# Generated by Django 4.2.2 on 2023-11-05 14:43

import currency_conversion.utils.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_rate', models.DecimalField(decimal_places=6, max_digits=10, validators=[currency_conversion.utils.validators.validate_positive_non_zero])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('from_currency', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='from_currency', to='currency_conversion.currency', verbose_name='from_currency')),
                ('to_currency', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='to_currency', to='currency_conversion.currency', verbose_name='to_currency')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='UserConversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('amt', models.DecimalField(decimal_places=6, max_digits=10, validators=[currency_conversion.utils.validators.validate_positive_non_zero])),
                ('status', models.CharField(choices=[('temporary', 'temporary'), ('permanent', 'permanent')], default='temporary', max_length=10)),
                ('result', models.DecimalField(decimal_places=8, max_digits=12)),
                ('rate', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='currency_conversion.exchangerate', verbose_name='Convertion_Rate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.AddIndex(
            model_name='exchangerate',
            index=models.Index(fields=['from_currency'], name='currency_co_from_cu_1d6ef5_idx'),
        ),
        migrations.AddIndex(
            model_name='exchangerate',
            index=models.Index(fields=['to_currency'], name='currency_co_to_curr_1c551c_idx'),
        ),
        migrations.AddIndex(
            model_name='exchangerate',
            index=models.Index(fields=['from_currency', 'to_currency'], name='currency_co_from_cu_1b41ff_idx'),
        ),
    ]
