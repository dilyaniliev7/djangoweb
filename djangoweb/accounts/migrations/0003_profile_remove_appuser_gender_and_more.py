# Generated by Django 4.2.9 on 2024-01-11 21:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import djangoweb.accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_appuser_first_name_alter_appuser_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(5), djangoweb.accounts.validators.validate_only_letters])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(5), djangoweb.accounts.validators.validate_only_letters])),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('DoNotShow', 'Do not show')], max_length=9)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='gender',
        ),
        migrations.AlterField(
            model_name='appuser',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
