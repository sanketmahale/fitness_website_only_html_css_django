# Generated by Django 2.2.2 on 2019-10-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='image',
            field=models.ImageField(default='', upload_to='meals'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='image',
            field=models.ImageField(default='', upload_to='trainers'),
            preserve_default=False,
        ),
    ]
