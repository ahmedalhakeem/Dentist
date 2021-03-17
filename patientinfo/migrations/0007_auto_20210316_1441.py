# Generated by Django 3.1.3 on 2021-03-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0006_auto_20210316_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='total_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='paid_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='remaining_cost',
            field=models.IntegerField(default=0),
        ),
    ]
