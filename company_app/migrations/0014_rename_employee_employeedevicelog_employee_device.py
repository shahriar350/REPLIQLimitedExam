# Generated by Django 4.1 on 2022-11-26 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_app', '0013_remove_employeedevices_log_employeedevicelog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeedevicelog',
            old_name='employee',
            new_name='employee_device',
        ),
    ]