# Generated by Django 2.1.3 on 2019-01-12 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('disc_number', models.PositiveIntegerField()),
                ('disc_total', models.PositiveIntegerField()),
                ('release_date', models.DateField()),
                ('label', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('date_formed', models.DateField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('release_date', models.DateField()),
                ('author', models.CharField(blank=True, default='', max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('artist', models.ManyToManyField(to='tickets.Artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='tickets.Genre')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AddField(
            model_name='album',
            name='songs',
            field=models.ManyToManyField(to='tickets.Song'),
        ),
    ]
