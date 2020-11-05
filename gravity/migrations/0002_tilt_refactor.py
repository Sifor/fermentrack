# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-18 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gravity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiltBridge',
            fields=[
                ('name', models.CharField(help_text='Name to identify this TiltBridge', max_length=64)),
                ('api_key', models.CharField(help_text="API key (a.k.a 'token') provided by the TiltBridge to identify/validate itself when it connects to the Raspberry Pi", max_length=64, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'TiltBridge',
                'verbose_name_plural': 'TiltBridges',
            },
        ),
        migrations.RemoveField(
            model_name='tiltconfiguration',
            name='average_period_secs',
        ),
        migrations.RemoveField(
            model_name='tiltconfiguration',
            name='bluetooth_device_id',
        ),
        migrations.RemoveField(
            model_name='tiltconfiguration',
            name='median_window_vals',
        ),
        migrations.RemoveField(
            model_name='tiltgravitycalibrationpoint',
            name='actual_value',
        ),
        migrations.RemoveField(
            model_name='tiltgravitycalibrationpoint',
            name='orig_value',
        ),
        migrations.AddField(
            model_name='tiltconfiguration',
            name='coefficients_up_to_date',
            field=models.BooleanField(default=True, help_text='Have the calibration points changed since the coefficient calculator was run?'),
        ),
        migrations.AddField(
            model_name='tiltconfiguration',
            name='connection_type',
            field=models.CharField(choices=[('Bluetooth', 'Bluetooth'), ('Bridge', 'TiltBridge')], default='Bluetooth', help_text='How should Fermentrack connect to this Tilt?', max_length=32),
        ),
        migrations.AddField(
            model_name='tiltconfiguration',
            name='grav_constant_term',
            field=models.FloatField(default=0.0, help_text='The constant term in the gravity calibration equation'),
        ),
        migrations.AddField(
            model_name='tiltconfiguration',
            name='grav_first_degree_coefficient',
            field=models.FloatField(default=1.0, help_text='The first degree coefficient in the gravity calibration equation'),
        ),
        migrations.AddField(
            model_name='tiltconfiguration',
            name='grav_second_degree_coefficient',
            field=models.FloatField(default=0.0, help_text='The second degree coefficient in the gravity calibration equation'),
        ),
        migrations.AddField(
            model_name='tiltconfiguration',
            name='smoothing_window_vals',
            field=models.IntegerField(default=70, help_text='Number of readings to include in the smoothing window.'),
        ),
        migrations.AddField(
            model_name='tiltgravitycalibrationpoint',
            name='actual_gravity',
            field=models.DecimalField(decimal_places=3, default=1.0, max_digits=5, verbose_name='Actual (Correct) Gravity value'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tiltgravitycalibrationpoint',
            name='tilt_measured_gravity',
            field=models.DecimalField(decimal_places=3, default=1.0, max_digits=5, verbose_name='Tilt Measured Gravity Value'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tiltconfiguration',
            name='polling_frequency',
            field=models.IntegerField(default=15, help_text='How frequently Fermentrack should update the temp/gravity reading'),
        ),
        migrations.AddField(
            model_name='tiltconfiguration',
            name='tiltbridge',
            field=models.ForeignKey(default=None, help_text='TiltBridge device to use (if any)', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gravity.TiltBridge'),
        ),
    ]
