# Generated by Django 3.0.6 on 2020-05-17 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0003_uzsakymas_uzsakymoeilute'),
    ]

    operations = [
        migrations.AddField(
            model_name='uzsakymoeilute',
            name='kiekis',
            field=models.IntegerField(null=True, verbose_name='Kiekis'),
        ),
    ]
