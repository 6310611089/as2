# Generated by Django 4.1.1 on 2022-09-16 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sID', models.IntegerField()),
                ('sName', models.CharField(max_length=100)),
            ],
        ),
    ]