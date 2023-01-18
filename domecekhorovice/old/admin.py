from django.apps import apps
from django.contrib.admin import ModelAdmin
from django.contrib.admin.sites import site


app_config = apps.get_app_config("old")

for Model in app_config.get_models():
    list_display = [f.name for f in Model._meta.fields]
    Admin = type(
        Model.__name__ + "Admin", (ModelAdmin,), {"list_display": list_display}
    )
    site.register(Model, Admin)
