# Generated by Django 4.0.2 on 2022-03-07 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_relying_party', '0006_alter_oidcauthentication_provider_configuration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oidcauthentication',
            name='provider_jwks',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]