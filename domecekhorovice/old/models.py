# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey("AuthPermission", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group", "permission"),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type", "codename"),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "auth_user"


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user", "group"),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user", "permission"),)


class CalendariumEvent(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    creation_date = models.DateTimeField()
    description = models.TextField()
    end_recurring_period = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=256)
    category = models.ForeignKey(
        "CalendariumEventcategory", models.DO_NOTHING, blank=True, null=True
    )
    created_by_id = models.IntegerField(blank=True, null=True)
    image = models.ForeignKey("FilerImage", models.DO_NOTHING, blank=True, null=True)
    rule = models.ForeignKey(
        "CalendariumRule", models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "calendarium_event"


class CalendariumEventcategory(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    color = models.CharField(max_length=6)
    parent = models.ForeignKey("self", models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "calendarium_eventcategory"


class CalendariumEventrelation(models.Model):
    object_id = models.IntegerField()
    relation_type = models.CharField(max_length=32, blank=True, null=True)
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
    event = models.ForeignKey(CalendariumEvent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "calendarium_eventrelation"


class CalendariumOccurrence(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    creation_date = models.DateTimeField()
    description = models.TextField()
    original_start = models.DateTimeField()
    original_end = models.DateTimeField()
    cancelled = models.BooleanField()
    title = models.CharField(max_length=256)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    event = models.ForeignKey(CalendariumEvent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "calendarium_occurrence"


class CalendariumRule(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    frequency = models.CharField(max_length=10)
    params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "calendarium_rule"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        "DjangoContentType", models.DO_NOTHING, blank=True, null=True
    )
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "django_admin_log"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"


class EasyThumbnailsSource(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "easy_thumbnails_source"
        unique_together = (("storage_hash", "name"),)


class EasyThumbnailsThumbnail(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()
    source = models.ForeignKey(EasyThumbnailsSource, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "easy_thumbnails_thumbnail"
        unique_together = (("storage_hash", "name", "source"),)


class EasyThumbnailsThumbnaildimensions(models.Model):
    thumbnail = models.OneToOneField(EasyThumbnailsThumbnail, models.DO_NOTHING)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "easy_thumbnails_thumbnaildimensions"


class FilerClipboard(models.Model):
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "filer_clipboard"


class FilerClipboarditem(models.Model):
    clipboard = models.ForeignKey(FilerClipboard, models.DO_NOTHING)
    file = models.ForeignKey("FilerFile", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "filer_clipboarditem"


class FilerFile(models.Model):
    file = models.CharField(max_length=255, blank=True, null=True)
    field_file_size = models.IntegerField(
        db_column="_file_size", blank=True, null=True
    )  # Field renamed because it started with '_'.
    sha1 = models.CharField(max_length=40)
    has_all_mandatory_data = models.BooleanField()
    original_filename = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    is_public = models.BooleanField()
    folder = models.ForeignKey("FilerFolder", models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    polymorphic_ctype = models.ForeignKey(
        DjangoContentType, models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "filer_file"


class FilerFolder(models.Model):
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey("self", models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "filer_folder"
        unique_together = (("parent", "name"),)


class FilerFolderpermission(models.Model):
    type = models.SmallIntegerField()
    everybody = models.BooleanField()
    can_edit = models.SmallIntegerField(blank=True, null=True)
    can_read = models.SmallIntegerField(blank=True, null=True)
    can_add_children = models.SmallIntegerField(blank=True, null=True)
    folder = models.ForeignKey(FilerFolder, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "filer_folderpermission"


class FilerImage(models.Model):
    file_ptr = models.OneToOneField(FilerFile, models.DO_NOTHING, primary_key=True)
    field_height = models.IntegerField(
        db_column="_height", blank=True, null=True
    )  # Field renamed because it started with '_'.
    field_width = models.IntegerField(
        db_column="_width", blank=True, null=True
    )  # Field renamed because it started with '_'.
    date_taken = models.DateTimeField(blank=True, null=True)
    default_alt_text = models.CharField(max_length=255, blank=True, null=True)
    default_caption = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    must_always_publish_author_credit = models.BooleanField()
    must_always_publish_copyright = models.BooleanField()
    subject_location = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "filer_image"


class FotogalerieGalleries(models.Model):
    title = models.CharField(max_length=500)
    desc = models.TextField()
    image = models.CharField(max_length=100)
    akce = models.ForeignKey("MainAkce", models.DO_NOTHING, blank=True, null=True)
    kurzy = models.ForeignKey("MainKurzy", models.DO_NOTHING, blank=True, null=True)
    lide = models.ForeignKey("MainLide", models.DO_NOTHING, blank=True, null=True)
    pracoviste = models.ForeignKey(
        "MainPracoviste", models.DO_NOTHING, blank=True, null=True
    )
    souteze = models.ForeignKey("MainSouteze", models.DO_NOTHING, blank=True, null=True)
    tabory = models.ForeignKey("MainTabory", models.DO_NOTHING, blank=True, null=True)
    zakladny = models.ForeignKey(
        "MainZakladny", models.DO_NOTHING, blank=True, null=True
    )
    datum = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fotogalerie_galleries"


class FotogaleriePhotos(models.Model):
    title = models.CharField(max_length=500)
    desc = models.CharField(max_length=500)
    image = models.CharField(max_length=100)
    gallery = models.ForeignKey(FotogalerieGalleries, models.DO_NOTHING)
    kronika = models.BooleanField()

    class Meta:
        managed = False
        db_table = "fotogalerie_photos"


class GdprGdpr(models.Model):
    text = models.TextField()
    rok = models.ForeignKey("MainRoky", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "gdpr_gdpr"


class GdprLoggdpr(models.Model):
    datum = models.DateTimeField()
    gdpr = models.ForeignKey(GdprGdpr, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "gdpr_loggdpr"


class HappeningsCancellation(models.Model):
    reason = models.CharField(max_length=255)
    date = models.DateField()
    event = models.ForeignKey("HappeningsEvent", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "happenings_cancellation"


class HappeningsCategory(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "happenings_category"


class HappeningsEvent(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    all_day = models.BooleanField()
    repeat = models.CharField(max_length=15)
    end_repeat = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    background_color = models.CharField(max_length=10)
    background_color_custom = models.CharField(max_length=6)
    font_color = models.CharField(max_length=10)
    font_color_custom = models.CharField(max_length=6)
    created_by_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "happenings_event"


class HappeningsEventCategories(models.Model):
    event = models.ForeignKey(HappeningsEvent, models.DO_NOTHING)
    category = models.ForeignKey(HappeningsCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "happenings_event_categories"
        unique_together = (("event", "category"),)


class HappeningsEventLocation(models.Model):
    event = models.ForeignKey(HappeningsEvent, models.DO_NOTHING)
    location = models.ForeignKey("HappeningsLocation", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "happenings_event_location"
        unique_together = (("event", "location"),)


class HappeningsEventTags(models.Model):
    event = models.ForeignKey(HappeningsEvent, models.DO_NOTHING)
    tag = models.ForeignKey("HappeningsTag", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "happenings_event_tags"
        unique_together = (("event", "tag"),)


class HappeningsLocation(models.Model):
    name = models.CharField(max_length=255)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    address_line_3 = models.CharField(max_length=255)
    state = models.CharField(max_length=63)
    city = models.CharField(max_length=63)
    zipcode = models.CharField(max_length=31)
    country = models.CharField(max_length=127)

    class Meta:
        managed = False
        db_table = "happenings_location"


class HappeningsTag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "happenings_tag"


class KaleidoskopKaleidoskop(models.Model):
    nazev = models.CharField(max_length=255)
    akce_od = models.DateTimeField()
    akce_do = models.DateTimeField()
    kde = models.CharField(max_length=255, blank=True, null=True)
    popis = models.TextField()
    popldeti = models.IntegerField()
    popldosp = models.IntegerField()
    poplrodina = models.IntegerField()
    image = models.CharField(max_length=100)
    plakat = models.CharField(max_length=100)
    plakat_home = models.BooleanField()
    priloha1 = models.CharField(max_length=255, blank=True, null=True)
    file1 = models.CharField(max_length=100, blank=True, null=True)
    priloha2 = models.CharField(max_length=255, blank=True, null=True)
    file2 = models.CharField(max_length=100, blank=True, null=True)
    priloha3 = models.CharField(max_length=255, blank=True, null=True)
    file3 = models.CharField(max_length=100, blank=True, null=True)
    poplatek = models.IntegerField()
    cena_clenove_rc = models.IntegerField()
    organizator = models.ForeignKey("MainLide", models.DO_NOTHING)
    rok = models.ForeignKey("MainRoky", models.DO_NOTHING)
    vs = models.CharField(max_length=4, blank=True, null=True)
    lektor = models.CharField(max_length=255, blank=True, null=True)
    publikovat = models.BooleanField()

    class Meta:
        managed = False
        db_table = "kaleidoskop_kaleidoskop"


class KaleidoskopKaleidoskopProKoho(models.Model):
    kaleidoskop = models.ForeignKey(KaleidoskopKaleidoskop, models.DO_NOTHING)
    pro_koho_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "kaleidoskop_kaleidoskop_pro_koho"
        unique_together = (("kaleidoskop", "pro_koho_id"),)


class KronikaKronika(models.Model):
    title = models.CharField(max_length=500)
    hodnoceni = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=100)
    datum = models.DateTimeField(blank=True, null=True)
    akce = models.ForeignKey("MainAkce", models.DO_NOTHING, blank=True, null=True)
    kurzy = models.ForeignKey("MainKurzy", models.DO_NOTHING, blank=True, null=True)
    souteze = models.ForeignKey("MainSouteze", models.DO_NOTHING, blank=True, null=True)
    tabory = models.ForeignKey("MainTabory", models.DO_NOTHING, blank=True, null=True)
    media = models.CharField(max_length=500, blank=True, null=True)
    pocet = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "kronika_kronika"


class KrouzkyKrouzkyprideti(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    datum_narozeni = models.DateField()
    misto_narozeni = models.CharField(max_length=100)
    narodnost = models.CharField(max_length=100)
    skola = models.CharField(max_length=100)
    trida = models.CharField(max_length=100)
    rc = models.CharField(max_length=100)
    zdravotni_pojistovna = models.CharField(max_length=100)
    adresa = models.CharField(max_length=500)
    psc = models.IntegerField()
    znevyhodneni = models.CharField(max_length=7)
    odchazet = models.BooleanField()
    otec_jmeno = models.CharField(max_length=100)
    otec_prijmeni = models.CharField(max_length=100)
    otec_telefon = models.CharField(max_length=100)
    otec_email = models.CharField(max_length=100)
    matka_jmeno = models.CharField(max_length=100)
    matka_prijmeni = models.CharField(max_length=100)
    matka_telefon = models.CharField(max_length=100)
    matka_email = models.CharField(max_length=100)
    datum = models.DateTimeField()
    ip = models.GenericIPAddressField(blank=True, null=True)
    krouzek = models.ForeignKey("MainKrouzky", models.DO_NOTHING, blank=True, null=True)
    upozorneni = models.TextField(blank=True, null=True)
    datum_active = models.DateTimeField(blank=True, null=True)
    datum_storno = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = "krouzky_krouzkyprideti"


class MainAkce(models.Model):
    nazev = models.CharField(max_length=255)
    akce_od = models.DateTimeField()
    akce_do = models.DateTimeField()
    kde = models.CharField(max_length=255, blank=True, null=True)
    popis = models.TextField()
    popldeti = models.IntegerField()
    popldosp = models.IntegerField()
    poplrodina = models.IntegerField()
    organizator_id = models.IntegerField()
    rok_id = models.IntegerField()
    image = models.CharField(max_length=100)
    plakat = models.CharField(max_length=100)
    plakat_home = models.BooleanField()
    priloha1 = models.CharField(max_length=255, blank=True, null=True)
    file1 = models.CharField(max_length=100, blank=True, null=True)
    file2 = models.CharField(max_length=100, blank=True, null=True)
    file3 = models.CharField(max_length=100, blank=True, null=True)
    priloha2 = models.CharField(max_length=255, blank=True, null=True)
    priloha3 = models.CharField(max_length=255, blank=True, null=True)
    poplatek = models.IntegerField()
    cena_clenove_rc = models.IntegerField()
    vs = models.CharField(max_length=4, blank=True, null=True)
    lektor = models.CharField(max_length=255, blank=True, null=True)
    file4 = models.CharField(max_length=100, blank=True, null=True)
    listina = models.CharField(max_length=255, blank=True, null=True)
    publikovat = models.BooleanField()

    class Meta:
        managed = False
        db_table = "main_akce"


class MainAkceProKoho(models.Model):
    akce = models.ForeignKey(MainAkce, models.DO_NOTHING)
    pro_koho_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "main_akce_pro_koho"
        unique_together = (("akce", "pro_koho_id"),)


class MainKestazeni(models.Model):
    nazev = models.CharField(max_length=500)
    popis = models.TextField()
    file = models.CharField(max_length=100)
    kam = models.IntegerField()
    trvale = models.BooleanField()
    roky = models.ForeignKey("MainRoky", models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "main_kestazeni"


class MainKontakt(models.Model):
    email = models.CharField(max_length=255)
    text = models.TextField()
    pokus = models.CharField(max_length=100)
    datum = models.DateTimeField(blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "main_kontakt"


class MainKrouzky(models.Model):
    nazev = models.CharField(max_length=255)
    zahajeni = models.CharField(max_length=255)
    zahajeni_public = models.BooleanField()
    pracoviste = models.ForeignKey("MainPracoviste", models.DO_NOTHING)
    ucebna = models.ForeignKey("MainUcebny", models.DO_NOTHING)
    popis = models.TextField()
    kapacita = models.IntegerField()
    krouzek_od = models.DateField()
    krouzek_do = models.DateField()
    rok_id = models.IntegerField()
    image = models.CharField(max_length=100)
    file1 = models.CharField(max_length=100, blank=True, null=True)
    file2 = models.CharField(max_length=100, blank=True, null=True)
    file3 = models.CharField(max_length=100, blank=True, null=True)
    priloha1 = models.CharField(max_length=255, blank=True, null=True)
    priloha2 = models.CharField(max_length=255, blank=True, null=True)
    priloha3 = models.CharField(max_length=255, blank=True, null=True)
    druh = models.IntegerField()
    vs = models.CharField(max_length=4, blank=True, null=True)
    lektor = models.CharField(max_length=255, blank=True, null=True)
    cena_deti3 = models.IntegerField()
    cenadosp = models.IntegerField()
    terminy = models.CharField(max_length=255, blank=True, null=True)
    cena_ms = models.IntegerField()
    cena_zs = models.IntegerField()
    poplatek_schuzka = models.IntegerField()
    publikovat = models.BooleanField()

    class Meta:
        managed = False
        db_table = "main_krouzky"


class MainKrouzkyProKoho(models.Model):
    krouzky = models.ForeignKey(MainKrouzky, models.DO_NOTHING)
    pro_koho_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "main_krouzky_pro_koho"
        unique_together = (("krouzky", "pro_koho_id"),)


class MainKrouzkyVedouci(models.Model):
    krouzky = models.ForeignKey(MainKrouzky, models.DO_NOTHING)
    lide = models.ForeignKey("MainLide", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "main_krouzky_vedouci"
        unique_together = (("krouzky", "lide"),)


class MainKurzy(models.Model):
    nazev = models.CharField(max_length=255)
    kurz_od = models.DateTimeField()
    kurz_do = models.DateTimeField()
    kde = models.CharField(max_length=255, blank=True, null=True)
    popis = models.TextField()
    popldeti = models.IntegerField()
    popldosp = models.IntegerField()
    poplrodina = models.IntegerField()
    organizator_id = models.IntegerField()
    rok_id = models.IntegerField()
    image = models.CharField(max_length=100)
    plakat = models.CharField(max_length=100)
    plakat_home = models.BooleanField()
    file1 = models.CharField(max_length=100, blank=True, null=True)
    file2 = models.CharField(max_length=100, blank=True, null=True)
    file3 = models.CharField(max_length=100, blank=True, null=True)
    priloha1 = models.CharField(max_length=255, blank=True, null=True)
    priloha2 = models.CharField(max_length=255, blank=True, null=True)
    priloha3 = models.CharField(max_length=255, blank=True, null=True)
    poplatek = models.IntegerField()
    poplatky_pro_pedagogy = models.IntegerField()
    vs = models.CharField(max_length=4, blank=True, null=True)
    lektor = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "main_kurzy"


class MainKurzyProKoho(models.Model):
    kurzy = models.ForeignKey(MainKurzy, models.DO_NOTHING)
    pro_koho_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "main_kurzy_pro_koho"
        unique_together = (("kurzy", "pro_koho_id"),)


class MainLide(models.Model):
    titul = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefon = models.CharField(max_length=50)
    mobil = models.CharField(max_length=50)
    adresa = models.TextField()
    ic = models.CharField(max_length=11)
    dic = models.CharField(max_length=11)
    bankovni_spojeni = models.CharField(max_length=100)
    rc = models.CharField(max_length=20)
    pojistovna = models.CharField(max_length=100)
    funkce = models.CharField(max_length=200)
    zarazeni = models.CharField(max_length=200)
    spoluprace = models.IntegerField()
    image = models.CharField(max_length=100)
    popis = models.TextField()
    order = models.IntegerField()
    misto_narozeni = models.CharField(max_length=100)
    pedagogicke_vzdelani = models.BooleanField()
    rodinny_stav = models.CharField(max_length=100)
    vzdelani = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "main_lide"


class MainPracoviste(models.Model):
    nazev = models.CharField(max_length=500)
    misto = models.CharField(max_length=500)
    adresa = models.TextField()
    ic = models.CharField(max_length=11)
    dic = models.CharField(max_length=11)
    bankovni_spojeni = models.CharField(max_length=100)
    vedouci_id = models.IntegerField()
    email = models.CharField(max_length=100)
    telefon = models.CharField(max_length=50)
    mobil = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    prohlidka = models.CharField(max_length=100)
    order = models.IntegerField()
    nazev_kratky = models.CharField(max_length=500, blank=True, null=True)
    mapa = models.CharField(max_length=1000)
    publikovat = models.BooleanField()

    class Meta:
        managed = False
        db_table = "main_pracoviste"


class MainRoky(models.Model):
    od = models.DateField()
    do = models.DateField()

    class Meta:
        managed = False
        db_table = "main_roky"


class MainSection(models.Model):
    title = models.CharField(max_length=255)
    href = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(blank=True, null=True)
    lang = models.IntegerField()
    view = models.BooleanField()

    class Meta:
        managed = False
        db_table = "main_section"


class MainSouteze(models.Model):
    sezona = models.IntegerField()
    nazev = models.CharField(max_length=255)
    soutez_od = models.DateTimeField()
    soutez_do = models.DateTimeField()
    kde = models.CharField(max_length=255, blank=True, null=True)
    popis = models.TextField()
    popldeti = models.IntegerField()
    popldosp = models.IntegerField()
    poplrodina = models.IntegerField()
    organizator_id = models.IntegerField()
    rok_id = models.IntegerField()
    image = models.CharField(max_length=100)
    plakat = models.CharField(max_length=100)
    plakat_home = models.BooleanField()
    file1 = models.CharField(max_length=100, blank=True, null=True)
    file2 = models.CharField(max_length=100, blank=True, null=True)
    file3 = models.CharField(max_length=100, blank=True, null=True)
    priloha1 = models.CharField(max_length=255, blank=True, null=True)
    priloha2 = models.CharField(max_length=255, blank=True, null=True)
    priloha3 = models.CharField(max_length=255, blank=True, null=True)
    poplatek = models.IntegerField()
    file4 = models.CharField(max_length=100, blank=True, null=True)
    listina = models.CharField(max_length=255, blank=True, null=True)
    publikovat = models.BooleanField()

    class Meta:
        managed = False
        db_table = "main_souteze"


class MainSoutezeProKoho(models.Model):
    souteze = models.ForeignKey(MainSouteze, models.DO_NOTHING)
    pro_koho_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "main_souteze_pro_koho"
        unique_together = (("souteze", "pro_koho_id"),)


class MainSubsection(models.Model):
    title = models.CharField(max_length=255)
    href = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(blank=True, null=True)
    section = models.ForeignKey(MainSection, models.DO_NOTHING)
    view = models.BooleanField()

    class Meta:
        managed = False
        db_table = "main_subsection"


class MainTabory(models.Model):
    zakladna = models.ForeignKey("MainZakladny", models.DO_NOTHING)
    nazev = models.CharField(max_length=255)
    tabor_od = models.DateField()
    tabor_do = models.DateField()
    popis = models.TextField()
    kapacita = models.IntegerField()
    vedouci_id = models.IntegerField()
    garant = models.CharField(max_length=255)
    image = models.CharField(max_length=100)
    file1 = models.CharField(max_length=100, blank=True, null=True)
    file2 = models.CharField(max_length=100, blank=True, null=True)
    file3 = models.CharField(max_length=100, blank=True, null=True)
    priloha1 = models.CharField(max_length=255, blank=True, null=True)
    priloha2 = models.CharField(max_length=255, blank=True, null=True)
    priloha3 = models.CharField(max_length=255, blank=True, null=True)
    cena_deti3 = models.IntegerField()
    cenadosp = models.IntegerField()
    vs = models.CharField(max_length=4, blank=True, null=True)
    cena_ms = models.IntegerField()
    cena_zs = models.IntegerField()
    publikovat = models.BooleanField()
    rok = models.ForeignKey(MainRoky, models.DO_NOTHING, blank=True, null=True)
    neprodavat = models.BooleanField()

    class Meta:
        managed = False
        db_table = "main_tabory"


class MainTaboryProKoho(models.Model):
    tabory = models.ForeignKey(MainTabory, models.DO_NOTHING)
    pro_koho_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "main_tabory_pro_koho"
        unique_together = (("tabory", "pro_koho_id"),)


class MainTaboryTerminy(models.Model):
    tabory_id = models.IntegerField()
    terminy_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "main_tabory_terminy"
        unique_together = (("tabory_id", "terminy_id"),)


class MainUcebny(models.Model):
    nazev = models.CharField(max_length=255)
    popis = models.TextField()
    pracoviste_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "main_ucebny"


class MainZakladny(models.Model):
    nazev = models.CharField(max_length=500)
    adresa = models.TextField()
    image = models.CharField(max_length=100)
    prohlidka = models.CharField(max_length=100)
    provoz_od = models.DateField()
    provoz_do = models.DateField()
    kontakt_id = models.IntegerField()
    rezervace = models.TextField()
    mapa = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = "main_zakladny"


class NapsaliNapsali(models.Model):
    co = models.CharField(max_length=1000, blank=True, null=True)
    datum = models.DateField()
    kde = models.CharField(max_length=500)
    popis = models.TextField()
    href = models.CharField(max_length=500)
    priloha1 = models.CharField(max_length=255, blank=True, null=True)
    file1 = models.CharField(max_length=100, blank=True, null=True)
    priloha2 = models.CharField(max_length=255, blank=True, null=True)
    file2 = models.CharField(max_length=100, blank=True, null=True)
    priloha3 = models.CharField(max_length=255, blank=True, null=True)
    file3 = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=100)
    kdo = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "napsali_napsali"


class NastaveniNastaveni(models.Model):
    splatnost = models.DateField()
    splatnost_tabory = models.DateField(blank=True, null=True)
    krouzky_cena_pulrok = models.IntegerField()
    krouzky_rok = models.ForeignKey(
        MainRoky, models.DO_NOTHING, blank=True, null=True, related_name="+"
    )
    souteze_rok = models.ForeignKey(
        MainRoky, models.DO_NOTHING, blank=True, null=True, related_name="+"
    )
    tabory_rok = models.ForeignKey(
        MainRoky, models.DO_NOTHING, blank=True, null=True, related_name="+"
    )

    class Meta:
        managed = False
        db_table = "nastaveni_nastaveni"


class NewsNews(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = "news_news"


class NotifyNotify(models.Model):
    akce = models.CharField(max_length=50)
    text = models.TextField()

    class Meta:
        managed = False
        db_table = "notify_notify"


class OrdersOrderitems(models.Model):
    nazev = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    product = models.IntegerField(blank=True, null=True)
    pay_half_year = models.BooleanField()
    order = models.ForeignKey("OrdersOrders", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "orders_orderitems"


class OrdersOrders(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pay_type = models.IntegerField()
    date_create = models.DateTimeField()
    date_paid = models.DateTimeField()
    pay_status = models.BooleanField()
    status = models.BooleanField()
    ip = models.GenericIPAddressField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    part_payment = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "orders_orders"


class OrdersPayments(models.Model):
    order = models.ForeignKey(OrdersOrders, models.DO_NOTHING)
    datum = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    pozn = models.TextField(blank=True, null=True)
    prihlaska = models.ForeignKey(
        "PrihlaskaPrihlaska", models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "orders_payments"


class PlakatyHomePlakatyhome(models.Model):
    image = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    my_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = "plakaty_home_plakatyhome"


class PrihlaskaKrouzkypresun(models.Model):
    poznamka = models.CharField(max_length=500, blank=True, null=True)
    krouzek_default = models.IntegerField(blank=True, null=True)
    krouzek = models.ForeignKey(MainKrouzky, models.DO_NOTHING)
    osoba = models.ForeignKey("PrihlaskaPrihlaska", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "prihlaska_krouzkypresun"


class PrihlaskaPrihlaska(models.Model):
    jmeno = models.CharField(max_length=100, blank=True, null=True)
    prijmeni = models.CharField(max_length=100, blank=True, null=True)
    misto_narozeni = models.CharField(max_length=100, blank=True, null=True)
    narodnost = models.CharField(max_length=100, blank=True, null=True)
    datum_narozeni = models.CharField(max_length=50, blank=True, null=True)
    zdravotni_pojistovna = models.CharField(max_length=100, blank=True, null=True)
    adresa = models.TextField(blank=True, null=True)
    psc = models.CharField(max_length=100, blank=True, null=True)
    rc = models.CharField(max_length=50, blank=True, null=True)
    znevyhodneni = models.CharField(max_length=7, blank=True, null=True)
    otec_jmeno = models.CharField(max_length=100, blank=True, null=True)
    otec_telefon = models.CharField(max_length=100, blank=True, null=True)
    otec_email = models.CharField(max_length=200, blank=True, null=True)
    matka_jmeno = models.CharField(max_length=100, blank=True, null=True)
    matka_telefon = models.CharField(max_length=100, blank=True, null=True)
    matka_email = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    datum = models.DateTimeField()
    datum_active = models.DateTimeField(blank=True, null=True)
    datum_storno = models.DateTimeField(blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    product = models.IntegerField(blank=True, null=True)
    pro_koho = models.IntegerField(blank=True, null=True)
    order_item = models.ForeignKey(
        OrdersOrderitems, models.DO_NOTHING, blank=True, null=True
    )
    skola = models.CharField(max_length=1000, blank=True, null=True)
    trida = models.CharField(max_length=1000, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    telefon = models.CharField(max_length=100, blank=True, null=True)
    upozorneni = models.TextField(blank=True, null=True)
    muze_nemuze = models.IntegerField()
    spat = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "prihlaska_prihlaska"


class ProKohoProKoho(models.Model):
    title = models.CharField(max_length=255)
    prihlasky = models.CharField(max_length=255, blank=True, null=True)
    search_box = models.IntegerField()

    class Meta:
        managed = False
        db_table = "pro_koho_pro_koho"


class ProfileProfile(models.Model):
    firma = models.CharField(max_length=100, blank=True, null=True)
    ic = models.CharField(max_length=20, blank=True, null=True)
    ulice = models.CharField(max_length=500, blank=True, null=True)
    mesto = models.CharField(max_length=100, blank=True, null=True)
    psc = models.CharField(max_length=10, blank=True, null=True)
    zeme = models.CharField(max_length=50, blank=True, null=True)
    telefon = models.CharField(max_length=50, blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    datum = models.DateTimeField(blank=True, null=True)
    reg_dodaci = models.BooleanField()
    d_jmeno = models.CharField(max_length=500, blank=True, null=True)
    d_ulice = models.CharField(max_length=500, blank=True, null=True)
    d_mesto = models.CharField(max_length=100, blank=True, null=True)
    d_psc = models.CharField(max_length=10, blank=True, null=True)
    d_zeme = models.CharField(max_length=50, blank=True, null=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "profile_profile"


class ScheduleCalendar(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = "schedule_calendar"


class ScheduleCalendarrelation(models.Model):
    object_id = models.IntegerField()
    distinction = models.CharField(max_length=20, blank=True, null=True)
    inheritable = models.BooleanField()
    calendar = models.ForeignKey(ScheduleCalendar, models.DO_NOTHING)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "schedule_calendarrelation"


class ScheduleEvent(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    end_recurring_period = models.DateTimeField(blank=True, null=True)
    calendar = models.ForeignKey(
        ScheduleCalendar, models.DO_NOTHING, blank=True, null=True
    )
    creator = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    rule = models.ForeignKey("ScheduleRule", models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "schedule_event"


class ScheduleEventrelation(models.Model):
    object_id = models.IntegerField()
    distinction = models.CharField(max_length=20, blank=True, null=True)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    event = models.ForeignKey(ScheduleEvent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "schedule_eventrelation"


class ScheduleOccurrence(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    cancelled = models.BooleanField()
    original_start = models.DateTimeField()
    original_end = models.DateTimeField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    event = models.ForeignKey(ScheduleEvent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "schedule_occurrence"


class ScheduleRule(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    frequency = models.CharField(max_length=10)
    params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "schedule_rule"


class TaboryTaboryprideti(models.Model):
    jmeno = models.CharField(max_length=100, blank=True, null=True)
    prijmeni = models.CharField(max_length=100, blank=True, null=True)
    datum_narozeni = models.CharField(max_length=50, blank=True, null=True)
    misto_narozeni = models.CharField(max_length=100, blank=True, null=True)
    adresa = models.TextField(blank=True, null=True)
    otec_jmeno = models.CharField(max_length=100, blank=True, null=True)
    otec_telefon = models.CharField(max_length=100, blank=True, null=True)
    matka_jmeno = models.CharField(max_length=100, blank=True, null=True)
    matka_telefon = models.CharField(max_length=100, blank=True, null=True)
    zdravotni_pojistovna = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    datum = models.DateTimeField()
    datum_active = models.DateTimeField(blank=True, null=True)
    datum_storno = models.DateTimeField(blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    order_item_id = models.IntegerField(blank=True, null=True)
    tabor = models.ForeignKey(MainTabory, models.DO_NOTHING, blank=True, null=True)
    matka_email = models.CharField(max_length=100, blank=True, null=True)
    narodnost = models.CharField(max_length=100, blank=True, null=True)
    otec_email = models.CharField(max_length=200, blank=True, null=True)
    psc = models.CharField(max_length=100, blank=True, null=True)
    stan_spat = models.CharField(max_length=100, blank=True, null=True)
    trida = models.CharField(max_length=100, blank=True, null=True)
    zakem_zs = models.CharField(max_length=100, blank=True, null=True)
    znevyhodneni = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tabory_taboryprideti"


class TaboryTaboryprirodicedeti(models.Model):
    jmeno = models.CharField(max_length=100, blank=True, null=True)
    prijmeni = models.CharField(max_length=100, blank=True, null=True)
    datum_narozeni = models.DateField(blank=True, null=True)
    misto_narozeni = models.CharField(max_length=100, blank=True, null=True)
    adresa = models.TextField(blank=True, null=True)
    psc = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    telefon = models.CharField(max_length=50, blank=True, null=True)
    dite1_jmeno = models.CharField(max_length=200, blank=True, null=True)
    dite1_datum_narozeni = models.CharField(max_length=50, blank=True, null=True)
    dite1_misto_narozeni = models.CharField(max_length=100, blank=True, null=True)
    dite1_zdravotni_pojistovna = models.CharField(max_length=100, blank=True, null=True)
    dite2_jmeno = models.CharField(max_length=200, blank=True, null=True)
    dite2_datum_narozeni = models.CharField(max_length=50, blank=True, null=True)
    dite2_misto_narozeni = models.CharField(max_length=100, blank=True, null=True)
    dite2_zdravotni_pojistovna = models.CharField(max_length=100, blank=True, null=True)
    stan = models.BooleanField()
    status = models.IntegerField()
    datum = models.DateTimeField()
    datum_active = models.DateTimeField(blank=True, null=True)
    datum_storno = models.DateTimeField(blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    order_item_id = models.IntegerField(blank=True, null=True)
    tabor = models.ForeignKey(MainTabory, models.DO_NOTHING, blank=True, null=True)
    dite3_datum_narozeni = models.CharField(max_length=50, blank=True, null=True)
    dite3_jmeno = models.CharField(max_length=200, blank=True, null=True)
    dite3_misto_narozeni = models.CharField(max_length=100, blank=True, null=True)
    dite3_zdravotni_pojistovna = models.CharField(max_length=100, blank=True, null=True)
    dite4_datum_narozeni = models.CharField(max_length=50, blank=True, null=True)
    dite4_jmeno = models.CharField(max_length=200, blank=True, null=True)
    dite4_misto_narozeni = models.CharField(max_length=100, blank=True, null=True)
    dite4_zdravotni_pojistovna = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tabory_taboryprirodicedeti"


class TaskTask(models.Model):
    ukol = models.CharField(max_length=1000)
    popis = models.TextField()
    priorita = models.IntegerField()
    datum = models.DateTimeField()
    datum_online = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "task_task"


class ThumbnailKvstore(models.Model):
    key = models.CharField(primary_key=True, max_length=200)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = "thumbnail_kvstore"
