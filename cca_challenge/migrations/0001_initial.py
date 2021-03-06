# Generated by Django 2.0 on 2018-11-24 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=50)),
                ('section_id', models.CharField(max_length=50)),
                ('instructor', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('room', models.CharField(max_length=50)),
                ('capacity', models.PositiveIntegerField()),
                ('registered', models.PositiveIntegerField()),
            ],
        ),
    ]
