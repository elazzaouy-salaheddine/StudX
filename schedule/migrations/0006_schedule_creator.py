# Generated by Django 2.1.3 on 2019-05-22 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedule', '0005_auto_20190522_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='slots_created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
