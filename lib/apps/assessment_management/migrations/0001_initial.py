# Generated by Django 5.0.6 on 2024-06-12 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Assessments', max_length=250)),
                ('assessment_type', models.CharField(choices=[('CS', 'Cognitive Status'), ('PA', 'Physical Assessment')], max_length=2)),
                ('assessment_date', models.DateField()),
                ('q_and_a', models.JSONField(default=list)),
                ('final_score', models.IntegerField()),
            ],
            options={
                'db_table': 'assessment',
            },
        ),
    ]