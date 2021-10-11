# Generated by Django 3.2.7 on 2021-10-11 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0009_apply_jobid'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='job_owner', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apply',
            name='cv',
            field=models.FileField(upload_to='Apply/'),
        ),
    ]