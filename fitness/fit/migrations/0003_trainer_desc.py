# Generated by Django 2.2.2 on 2019-10-09 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0002_auto_20191006_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='desc',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
    ]