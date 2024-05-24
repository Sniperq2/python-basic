# Generated by Django 5.0.3 on 2024-05-22 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0002_auto_20240522_1106'),
    ]

    def insert_default_claims_types(apps, schema_editor):
        claim_status = apps.get_model('claims', 'ClaimType')
        status_list = ["Мусор, листва", "Ремонт покрытия дорог", "Тротуар", "Озеленение двора", "Дорожный знак"]
        for s in status_list:
            cl_status = claim_status(name=s)
            cl_status.save()

    operations = [
        migrations.RunPython(insert_default_claims_types),
    ]
