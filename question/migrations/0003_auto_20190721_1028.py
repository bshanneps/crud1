# Generated by Django 2.2.3 on 2019-07-21 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20190721_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='publish_date',
            new_name='date',
        ),
    ]