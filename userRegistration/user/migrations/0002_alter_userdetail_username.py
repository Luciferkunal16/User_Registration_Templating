# Generated by Django 4.0.3 on 2022-03-02 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
