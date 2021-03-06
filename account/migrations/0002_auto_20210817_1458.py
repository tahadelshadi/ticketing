# Generated by Django 3.2.6 on 2021-08-17 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_accountants',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_sup',
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='نام')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator+', to=settings.AUTH_USER_MODEL, verbose_name='سازنده')),
            ],
            options={
                'verbose_name': 'دپارتمان',
                'verbose_name_plural': 'دپارتمان ها',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.department', verbose_name='دپارتمان'),
        ),
    ]
