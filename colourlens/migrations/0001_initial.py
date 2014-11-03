# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accession_number', models.CharField(unique=True, max_length=100)),
                ('title', models.CharField(max_length=100, blank=True)),
                ('artist', models.CharField(max_length=100, blank=True)),
                ('year', models.IntegerField(db_index=True, null=True, blank=True)),
                ('url', models.URLField(blank=True)),
                ('image_url', models.URLField(blank=True)),
                ('institution', models.CharField(db_index=True, max_length=10, blank=True)),
                ('proportions', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, db_index=True)),
                ('hex_value', models.CharField(unique=True, max_length=10, blank=True)),
                ('red', models.IntegerField(null=True)),
                ('green', models.IntegerField(null=True)),
                ('blue', models.IntegerField(null=True)),
                ('hue', models.IntegerField(db_index=True, null=True, blank=True)),
                ('elite', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ColourDistance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('red', models.IntegerField(null=True)),
                ('green', models.IntegerField(null=True)),
                ('blue', models.IntegerField(null=True)),
                ('distance', models.DecimalField(null=True, max_digits=5, decimal_places=2, db_index=True)),
                ('prominence', models.DecimalField(null=True, max_digits=3, decimal_places=2, db_index=True)),
                ('presence', models.DecimalField(null=True, max_digits=5, decimal_places=2, db_index=True)),
                ('artwork', models.ForeignKey(to='colourlens.Artwork')),
                ('colour', models.ForeignKey(to='colourlens.Colour')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='colourdistance',
            unique_together=set([('artwork', 'colour')]),
        ),
        migrations.AddField(
            model_name='artwork',
            name='colours',
            field=models.ManyToManyField(to='colourlens.Colour', through='colourlens.ColourDistance'),
            preserve_default=True,
        ),
    ]
