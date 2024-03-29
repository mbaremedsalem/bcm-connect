# Generated by Django 5.0.2 on 2024-02-23 18:18

import api.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstname', models.CharField(blank=True, max_length=50)),
                ('lastname', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(max_length=16, unique=True)),
                ('username', models.CharField(max_length=16, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('post', models.CharField(max_length=200, null=True)),
                ('role', models.CharField(choices=[('Caissier', 'Caissier'), ('ChefAgence', 'ChefAgence')], default='Caissier', max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('verified', models.BooleanField(default=False)),
                ('restricted', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_blocked', models.BooleanField(default=False)),
                ('number_attempt', models.IntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Caissier',
            fields=[
                ('useraub_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(null=True, upload_to=api.models.image_uoload_profile)),
            ],
            options={
                'abstract': False,
            },
            bases=('api.useraub',),
        ),
        migrations.CreateModel(
            name='ChefAgence',
            fields=[
                ('useraub_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(null=True, upload_to=api.models.image_uoload_profile)),
            ],
            options={
                'abstract': False,
            },
            bases=('api.useraub',),
        ),
    ]
