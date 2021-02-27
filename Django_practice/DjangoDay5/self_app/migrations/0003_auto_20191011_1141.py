# Generated by Django 2.0.6 on 2019-10-11 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('self_app', '0002_spy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'wei_relations',
            },
        ),
        migrations.CreateModel(
            name='WeiUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'weiusers',
            },
        ),
        migrations.AddField(
            model_name='relation',
            name='fans',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fans_relations', to='self_app.WeiUser'),
        ),
        migrations.AddField(
            model_name='relation',
            name='followed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followd_relations', to='self_app.WeiUser'),
        ),
    ]