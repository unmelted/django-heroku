# Generated by Django 3.1.5 on 2021-02-13 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='anwer',
            new_name='answer',
        ),
    ]
