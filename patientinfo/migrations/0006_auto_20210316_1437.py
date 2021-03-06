# Generated by Django 3.1.3 on 2021-03-16 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0005_auto_20210315_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extra_appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_appointment', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='treatment',
            name='new_appointment',
            field=models.ManyToManyField(related_name='extra_appoint', to='patientinfo.Extra_appointment'),
        ),
    ]
