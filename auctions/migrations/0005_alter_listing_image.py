# Generated by Django 4.1.4 on 2022-12-13 20:43

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_listing_current_price_alter_listing_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[500, None], upload_to='images/'),
        ),
    ]