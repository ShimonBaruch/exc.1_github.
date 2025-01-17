# Generated by Django 4.1.3 on 2022-12-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdoctor',
            name='department',
            field=models.CharField(choices=[('1', 'Otorhinolaryngology'), ('2', 'Cardiology'), ('3', 'Oncology'), ('4', 'Dermatologist'), ('5', 'Endocrinologist'), ('6', 'Gastroenterologist'), ('7', 'Hematologist'), ('8', 'Nephrologists'), ('9', 'Neurologists'), ('10', 'Ophthalmologist')], max_length=50),
        ),
        migrations.AlterField(
            model_name='userpatient',
            name='priority',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
