# Generated by Django 3.1.3 on 2021-03-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0002_auto_20210313_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='appointment',
            field=models.ManyToManyField(related_name='patient_treat', to='patientinfo.Appointment'),
        ),
    ]