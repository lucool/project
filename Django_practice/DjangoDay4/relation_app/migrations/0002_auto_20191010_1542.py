# Generated by Django 2.0.6 on 2019-10-10 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relation_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardno', models.CharField(max_length=20, unique=True)),
                ('color', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'cards',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'person',
            },
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allstudents', to='relation_app.School'),
        ),
        migrations.AddField(
            model_name='card',
            name='per',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='relation_app.Person'),
        ),
    ]
