# Generated by Django 3.2.7 on 2021-09-30 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], default='meow', max_length=100)),
                ('test', models.CharField(default='meow', max_length=100)),
                ('slug', models.CharField(max_length=10, null=True, unique=True)),
            ],
        ),
    ]