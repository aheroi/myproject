# Generated by Django 4.0.6 on 2022-08-16 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfinpages', '0003_alter_balance_options_balance_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='income',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='outcome',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]