# Generated by Django 4.0.6 on 2022-08-16 07:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myfinpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('date', models.DateTimeField()),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'CURRENT'), (2, 'SAVING')], default=1)),
                ('notes', models.CharField(default='-', max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Balances',
            },
        ),
        migrations.RemoveField(
            model_name='income',
            name='category',
        ),
        migrations.RemoveField(
            model_name='outcome',
            name='category',
        ),
        migrations.AddField(
            model_name='income',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 8, 16, 7, 30, 17, 452336, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='income',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'SALARY'), (2, 'BONUS'), (3, 'OTHER')], default=1),
        ),
        migrations.AddField(
            model_name='outcome',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 8, 16, 7, 30, 26, 720168, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='outcome',
            name='notes',
            field=models.CharField(default='-', max_length=64),
        ),
        migrations.AddField(
            model_name='outcome',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'BILLS'), (2, 'GROCERIES'), (3, 'CLOTHES'), (4, 'STUDY'), (5, 'SPORT'), (6, 'FUN'), (7, 'HEALTHY'), (8, 'HOME'), (9, 'FAMILY'), (10, 'GIFT'), (11, 'OTHER'), (12, 'SAVING')], default=1),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='income',
            name='notes',
            field=models.CharField(default='-', max_length=64),
        ),
        migrations.AlterField(
            model_name='outcome',
            name='date',
            field=models.DateTimeField(),
        ),
    ]