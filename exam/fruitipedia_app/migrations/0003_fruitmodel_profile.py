# Generated by Django 4.2.2 on 2023-06-24 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fruitipedia_app', '0002_alter_profilemodel_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruitmodel',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fruitipedia_app.profilemodel'),
            preserve_default=False,
        ),
    ]
