from django.contrib.auth.hashers import make_password
from django.db import migrations


DEMO_USERNAME = "admin"
DEMO_PASSWORD = "admin*123"


def create_demo_user(apps, schema_editor):
    User = apps.get_model("auth", "User")
    user, _ = User.objects.get_or_create(
        username=DEMO_USERNAME,
        defaults={
            "is_staff": False,
            "is_superuser": False,
            "is_active": True,
        },
    )
    user.password = make_password(DEMO_PASSWORD)
    user.is_active = True
    user.is_staff = False
    user.is_superuser = False
    user.save(update_fields=["password", "is_active", "is_staff", "is_superuser"])


def remove_demo_user(apps, schema_editor):
    User = apps.get_model("auth", "User")
    User.objects.filter(username=DEMO_USERNAME, is_staff=False, is_superuser=False).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_demo_user, remove_demo_user),
    ]
