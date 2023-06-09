# Generated by Django 4.1.7 on 2023-03-23 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_medicalrecord_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalrecord',
            name='date_of_diagnosis',
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='cough',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='fever',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='head_ache',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='injuries',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='malaria',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='stomach_ache',
            field=models.CharField(max_length=255),
        ),
    ]
