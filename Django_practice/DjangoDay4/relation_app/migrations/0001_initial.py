# Generated by Django 2.0.6 on 2019-10-10 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('history', models.TextField(null=True)),
            ],
            options={
                'db_table': 'schools',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=10)),
                ('score', models.FloatField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relation_app.School')),
            ],
            options={
                'db_table': 'stus',
            },
        ),
    ]
