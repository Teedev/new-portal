# Generated by Django 5.1.7 on 2025-03-11 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BuildsecM",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("contract_no", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=255)),
                ("company_name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("contract_advert", models.FileField(upload_to="contracts/")),
                ("company_profile", models.FileField(upload_to="contracts/")),
                ("contract_agreement", models.FileField(upload_to="contracts/")),
                (
                    "variations",
                    models.FileField(blank=True, null=True, upload_to="contracts/"),
                ),
                ("applications", models.FileField(upload_to="contracts/")),
                ("certificate_no_objection", models.FileField(upload_to="contracts/")),
                ("award_certificate", models.FileField(upload_to="contracts/")),
                ("completion_certificate", models.FileField(upload_to="contracts/")),
                ("drawing", models.FileField(upload_to="contracts/")),
                ("certificate_valuation", models.FileField(upload_to="contracts/")),
                ("approvals", models.FileField(upload_to="contracts/")),
            ],
        ),
        migrations.CreateModel(
            name="CivilsectionM",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("contract_no", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=255)),
                ("company_name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("contract_advert", models.FileField(upload_to="contracts/")),
                ("company_profile", models.FileField(upload_to="contracts/")),
                ("contract_agreement", models.FileField(upload_to="contracts/")),
                (
                    "variations",
                    models.FileField(blank=True, null=True, upload_to="contracts/"),
                ),
                ("applications", models.FileField(upload_to="contracts/")),
                ("certificate_no_objection", models.FileField(upload_to="contracts/")),
                ("award_certificate", models.FileField(upload_to="contracts/")),
                ("completion_certificate", models.FileField(upload_to="contracts/")),
                ("drawing", models.FileField(upload_to="contracts/")),
                ("certificate_valuation", models.FileField(upload_to="contracts/")),
                ("approvals", models.FileField(upload_to="contracts/")),
            ],
        ),
        migrations.CreateModel(
            name="ElectsectionM",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("contract_no", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=255)),
                ("company_name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("contract_advert", models.FileField(upload_to="contracts/")),
                ("company_profile", models.FileField(upload_to="contracts/")),
                ("contract_agreement", models.FileField(upload_to="contracts/")),
                (
                    "variations",
                    models.FileField(blank=True, null=True, upload_to="contracts/"),
                ),
                ("applications", models.FileField(upload_to="contracts/")),
                ("certificate_no_objection", models.FileField(upload_to="contracts/")),
                ("award_certificate", models.FileField(upload_to="contracts/")),
                ("completion_certificate", models.FileField(upload_to="contracts/")),
                ("drawing", models.FileField(upload_to="contracts/")),
                ("certificate_valuation", models.FileField(upload_to="contracts/")),
                ("approvals", models.FileField(upload_to="contracts/")),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="WorkGenM",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("contract_no", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=255)),
                ("company_name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("contract_advert", models.FileField(upload_to="contracts/")),
                ("company_profile", models.FileField(upload_to="contracts/")),
                ("contract_agreement", models.FileField(upload_to="contracts/")),
                (
                    "variations",
                    models.FileField(blank=True, null=True, upload_to="contracts/"),
                ),
                ("applications", models.FileField(upload_to="contracts/")),
                ("certificate_no_objection", models.FileField(upload_to="contracts/")),
                ("award_certificate", models.FileField(upload_to="contracts/")),
                ("completion_certificate", models.FileField(upload_to="contracts/")),
                ("drawing", models.FileField(upload_to="contracts/")),
                ("certificate_valuation", models.FileField(upload_to="contracts/")),
                ("approvals", models.FileField(upload_to="contracts/")),
            ],
        ),
        migrations.AlterField(
            model_name="property",
            name="coordinate",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="property",
            name="cost",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="property",
            name="location",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="property",
            name="passport",
            field=models.FileField(upload_to="properties/"),
        ),
        migrations.AlterField(
            model_name="property",
            name="property_no",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="property",
            name="property_type",
            field=models.CharField(max_length=255),
        ),
    ]
