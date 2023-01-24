import html
import re
from collections import defaultdict as Defaultdict
from datetime import date as Date
from datetime import timedelta as Timedelta
from itertools import chain
from typing import Dict

from django.core.management.base import BaseCommand
from leprikon.models.agegroup import AgeGroup
from leprikon.models.courses import Course
from leprikon.models.events import Event
from leprikon.models.place import Place
from leprikon.models.roles import Contact, Leader
from leprikon.models.schoolyear import SchoolYear, SchoolYearDivision, SchoolYearPeriod
from leprikon.models.subjects import SubjectType
from user_unique_email.models import User

from domecekhorovice.old.models import *


class Command(BaseCommand):
    help = "Imports old data"
    users: Dict[int, User] = {}
    users_by_email: Dict[str, User] = {}
    school_years: Dict[int, SchoolYear] = {}
    school_years_by_year: Dict[int, SchoolYear] = {}
    school_year_divisions: Dict[int, SchoolYearDivision] = {}
    age_groups: Dict[int, AgeGroup] = {}
    leaders: Dict[int, Leader] = {}
    places_by_pracoviste: Dict[int, Place] = {}
    places_by_zakladna: Dict[int, Place] = {}
    course: SubjectType
    camp: SubjectType
    event: SubjectType
    courses: Dict[int, Course] = {}
    camps: Dict[int, Event] = {}
    events: Dict[int, Event] = {}

    strip_tags_re = re.compile("<[^>]*>")

    def handle(self, *args, **options):
        self.course = SubjectType.objects.get(subject_type=SubjectType.COURSE, slug="krouzky")
        self.camp = SubjectType.objects.get(subject_type=SubjectType.EVENT, slug="tabory")
        self.event = SubjectType.objects.get(subject_type=SubjectType.EVENT, slug="akce")
        self.competition = SubjectType.objects.get(subject_type=SubjectType.EVENT, slug="souteze")
        self.import_users()
        self.import_years()
        self.import_age_groups()
        self.import_leaders()
        self.import_places()
        self.import_courses()
        self.import_camps()
        self.import_events()
        self.import_competitions()
        self.fix_leader_school_years()

    def import_users(self):
        self.users_by_email = {u.email: u for u in User.objects.all()}
        for user in AuthUser.objects.exclude(email="").exclude(email=None).order_by("-id").iterator():
            email = user.email.lower()
            if email not in self.users_by_email:
                user_data = user.__dict__.copy()
                del user_data["_state"], user_data["id"], user_data["email"]
                self.users_by_email[email] = User.objects.create(email=email, **user_data)
                self.stdout.write(self.style.SUCCESS(f"Successfully imported user {self.users_by_email[email]}"))
            else:
                self.stdout.write(self.style.HTTP_INFO(f"user {self.users_by_email[email]} already imported"))
            self.users[user.pk] = self.users_by_email[email]

    def import_years(self):
        for id, year in MainRoky.objects.order_by("od").values_list("id", "od__year"):
            self.school_years[id], new = SchoolYear.objects.get_or_create(year=year)
            self.school_years_by_year[year] = self.school_years[id]
            if new:
                self.stdout.write(self.style.SUCCESS(f"Successfully imported year {self.school_years[id]}"))
            self.school_year_divisions[id], new = SchoolYearDivision.objects.get_or_create(
                school_year=self.school_years[id],
                name="školní rok",
                price_unit_name="školní rok",
            )
            if new:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully imported school year division {self.school_year_divisions[id]}")
                )
                SchoolYearPeriod.objects.create(
                    school_year_division=self.school_year_divisions[id],
                    name="školní rok",
                    start=Date(year, 9, 1),
                    end=Date(year + 1, 6, 30),
                    due_from=Date(year, 6, 1),
                    due_date=Date(year, 10, 15),
                )

    def import_age_groups(self):
        for prokoho in ProKohoProKoho.objects.all():
            self.age_groups[prokoho.pk], new = AgeGroup.objects.get_or_create(
                name=prokoho.title[:50], defaults=dict(order=prokoho.search_box)
            )
            if new:
                self.style.SUCCESS(f"Successfully imported age group {self.age_groups[prokoho.pk]}")

    def import_leaders(self):
        email_counts = Defaultdict(int)
        for email in MainLide.objects.values_list("email", flat=True):
            email_counts[email.lower()] += 1
        for osoba in MainLide.objects.iterator():
            email = osoba.email.lower()
            user = self.users_by_email.get(email)
            if email_counts[email] > 1:
                if user is not None and (user.first_name != osoba.first_name or user.last_name != osoba.last_name):
                    user = None
                    email = f"unknown-{osoba.pk}@domecekhorovice.cz"
            if user is None:
                user = User.objects.create(
                    email=email,
                    username=email,
                    first_name=osoba.first_name,
                    last_name=osoba.last_name,
                )
                self.users_by_email[email] = user
                self.stdout.write(self.style.SUCCESS(f"Successfully imported user {user}"))
            if user.first_name != osoba.first_name or user.last_name != osoba.last_name:
                user.first_name = osoba.first_name
                user.last_name = osoba.last_name
                user.save()
            leader, new = Leader.objects.get_or_create(user=user)
            self.leaders[osoba.pk] = leader
            # store original (even duplicit) contact email
            Contact.objects.get_or_create(
                leader=leader, contact_type="email", contact=osoba.email.lower(), defaults=dict(order=1)
            )
            if osoba.telefon:
                Contact.objects.get_or_create(
                    leader=leader, contact_type="phone", contact=osoba.telefon, defaults=dict(order=2)
                )
            if osoba.mobil:
                Contact.objects.get_or_create(
                    leader=leader, contact_type="phone", contact=osoba.mobil, defaults=dict(order=2)
                )
            if osoba.adresa:
                Contact.objects.get_or_create(
                    leader=leader,
                    contact_type="address",
                    contact=html.unescape(self.strip_tags_re.sub("", osoba.adresa)),
                    defaults=dict(order=3),
                )
            if new:
                self.style.SUCCESS(f"Successfully imported leader {self.leaders[osoba.pk]}")

    def import_places(self):
        for pracoviste in MainPracoviste.objects.all():
            self.places_by_pracoviste[pracoviste.pk], new = Place.objects.get_or_create(
                name=pracoviste.nazev[:50], defaults=dict(place=pracoviste.misto)
            )
            if new:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully imported place {self.places_by_pracoviste[pracoviste.pk]}")
                )
        for zakladna in MainZakladny.objects.all():
            self.places_by_zakladna[zakladna.pk], new = Place.objects.get_or_create(name=zakladna.nazev[:50])
            if new:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully imported place {self.places_by_zakladna[zakladna.pk]}")
                )

    def import_courses(self):
        for krouzek in MainKrouzky.objects.order_by("id").iterator():
            course, new = Course.objects.get_or_create(
                school_year=self.school_years[krouzek.rok_id],
                subject_type=self.course,
                place=self.places_by_pracoviste[krouzek.pracoviste_id],
                name=krouzek.nazev[:150],
                defaults=dict(
                    registration_type="P",
                    description=krouzek.popis,
                    max_participants_count=krouzek.kapacita,
                    public=krouzek.publikovat,
                    school_year_division=self.school_year_divisions[krouzek.rok_id],
                ),
            )
            course.age_groups.set(
                [self.age_groups[pk.pro_koho_id] for pk in MainKrouzkyProKoho.objects.filter(krouzky=krouzek)]
            )
            course.leaders.set(
                [
                    self.leaders[kv.lide_id]
                    for kv in MainKrouzkyVedouci.objects.filter(krouzky=krouzek)
                    if kv.lide_id in self.leaders
                ]
            )
            self.courses[krouzek.pk] = course
            if new:
                self.stdout.write(self.style.SUCCESS(f"Successfully imported course {course}"))
            else:
                self.stdout.write(self.style.HTTP_INFO(f"course {course} already imported"))

    def get_school_year(self, date: Date) -> SchoolYear:
        year = date.year - 1 if date.month < 9 else date.year
        if year not in self.school_years_by_year:
            self.school_years_by_year[year] = SchoolYear.objects.create(year=year)
        return self.school_years_by_year[year]

    def import_camps(self):
        for tabor in MainTabory.objects.order_by("id").iterator():
            event, new = Event.objects.get_or_create(
                school_year=self.get_school_year(tabor.tabor_od),
                subject_type=self.camp,
                place=self.places_by_zakladna[tabor.zakladna_id],
                name=tabor.nazev[:150],
                start_date=tabor.tabor_od,
                end_date=tabor.tabor_do,
                defaults=dict(
                    registration_type="P",
                    description=tabor.popis,
                    max_participants_count=tabor.kapacita,
                    public=tabor.publikovat,
                    due_from=tabor.tabor_od - Timedelta(days=365),
                    due_date=tabor.tabor_od - Timedelta(days=30),
                ),
            )
            event.age_groups.set(
                [self.age_groups[pk.pro_koho_id] for pk in MainTaboryProKoho.objects.filter(tabory=tabor)]
            )
            event.leaders.set([self.leaders[tabor.vedouci_id]] if tabor.vedouci_id in self.leaders else [])
            self.camps[tabor.pk] = event
            if new:
                self.stdout.write(self.style.SUCCESS(f"Successfully imported event {event}"))
            else:
                self.stdout.write(self.style.HTTP_INFO(f"event {event} already imported"))

    def import_events(self):
        for akce in MainAkce.objects.order_by("id").iterator():
            event, new = Event.objects.get_or_create(
                school_year=self.school_years[akce.rok_id],
                subject_type=self.camp,
                name=akce.nazev[:150],
                start_date=akce.akce_od,
                end_date=akce.akce_do,
                defaults=dict(
                    registration_type="P",
                    description=akce.popis,
                    public=akce.publikovat,
                    due_from=akce.akce_od - Timedelta(days=365),
                    due_date=akce.akce_od - Timedelta(days=30),
                ),
            )
            event.age_groups.set(
                [
                    self.age_groups[pk.pro_koho_id]
                    for pk in MainAkceProKoho.objects.filter(akce=akce)
                    if pk.pro_koho_id in self.age_groups
                ]
            )
            event.leaders.set([self.leaders[akce.organizator_id]] if akce.organizator_id in self.leaders else [])
            self.camps[akce.pk] = event
            if new:
                self.stdout.write(self.style.SUCCESS(f"Successfully imported event {event}"))
            else:
                self.stdout.write(self.style.HTTP_INFO(f"event {event} already imported"))

    def import_competitions(self):
        for soutez in MainSouteze.objects.order_by("id").iterator():
            event, new = Event.objects.get_or_create(
                school_year=self.school_years[soutez.rok_id],
                subject_type=self.competition,
                name=soutez.nazev[:150],
                start_date=soutez.soutez_od,
                end_date=soutez.soutez_do,
                defaults=dict(
                    registration_type="P",
                    description=soutez.popis,
                    public=soutez.publikovat,
                    due_from=soutez.soutez_od - Timedelta(days=365),
                    due_date=soutez.soutez_od - Timedelta(days=30),
                ),
            )
            event.age_groups.set(
                [
                    self.age_groups[pk.pro_koho_id]
                    for pk in MainSoutezeProKoho.objects.filter(souteze=soutez)
                    if pk.pro_koho_id in self.age_groups
                ]
            )
            event.leaders.set([self.leaders[soutez.organizator_id]] if soutez.organizator_id in self.leaders else [])
            self.camps[soutez.pk] = event
            if new:
                self.stdout.write(self.style.SUCCESS(f"Successfully imported event {event}"))
            else:
                self.stdout.write(self.style.HTTP_INFO(f"event {event} already imported"))

    def fix_leader_school_years(self):
        for leader in Leader.objects.all():
            leader.school_years.set(
                set(
                    chain(
                        leader.school_years.values_list("id", flat=True),
                        leader.subjects.values_list("school_year_id", flat=True),
                    )
                )
            )
