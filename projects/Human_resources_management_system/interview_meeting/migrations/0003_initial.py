# Generated by Django 4.2 on 2024-02-04 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personels', '0001_initial'),
        ('interview_meeting', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='applier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interview',
            name='interviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interviews', to='personels.personel'),
        ),
    ]
