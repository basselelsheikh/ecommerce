# Generated by Django 4.1.4 on 2022-12-13 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_remove_user_bio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
