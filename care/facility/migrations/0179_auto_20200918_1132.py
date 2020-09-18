# Generated by Django 2.2.11 on 2020-09-18 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0178_auto_20200916_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='facility_type',
            field=models.IntegerField(choices=[(1, 'Educational Inst'), (2, 'Private Hospital'), (3, 'Other'), (4, 'Hostel'), (5, 'Hotel'), (6, 'Lodge'), (7, 'TeleMedicine'), (8, 'Govt Hospital'), (9, 'Labs'), (800, 'Primary Health Centres'), (801, '24x7 Public Health Centres'), (802, 'Family Health Centres'), (803, 'Community Health Centres'), (820, 'Urban Primary Health Center'), (830, 'Taluk Hospitals'), (831, 'Taluk Headquarters Hospitals'), (840, 'Women and Child Health Centres'), (850, 'General hospitals'), (860, 'District Hospitals'), (870, 'Govt Medical College Hospitals'), (950, 'Corona Testing Labs'), (1000, 'Corona Care Centre'), (1100, 'First Line Treatment Centre'), (1200, 'Second Line Treatment Center'), (1300, 'Shifting Centre'), (1400, 'Covid Management Center')]),
        ),
    ]
