# Generated by Django 2.1.5 on 2019-01-25 13:57

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0006_playerinteam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('match_date', models.DateTimeField()),
                ('score', models.PositiveSmallIntegerField(choices=[(1, '3-0'), (2, '3-1'), (3, '3-2'), (4, '2-3'), (5, '1-3'), (6, '0-3')])),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='league.TeamSeason')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='league.TeamSeason')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
