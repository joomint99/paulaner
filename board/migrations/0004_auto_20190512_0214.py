# Generated by Django 2.1.8 on 2019-05-11 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20190512_0210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dong',
            old_name='pub_date',
            new_name='date',
        ),
    ]