# Generated by Django 2.2.2 on 2019-06-15 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190613_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='comments',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
