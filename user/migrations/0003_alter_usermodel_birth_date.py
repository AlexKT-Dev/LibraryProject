# Generated by Django 4.1.3 on 2022-12-14 11:10

import datetime
from django.db import migrations, models
import user.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_usermodel_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 14, 11, 10, 41, 972777, tzinfo=datetime.timezone.utc), validators=[user.validators.validate_age], verbose_name='Date of birth'),
        ),
    ]
