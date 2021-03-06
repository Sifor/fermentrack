# Generated by Django 3.0.5 on 2020-05-25 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_squashed_0009_auto_20180709_0256'),
        ('gravity', '0002_brewfather_updates'),
        ('external_push', '0001_squashed_0007_fix_thingspeak'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewfatherpushtarget',
            name='brewpi_to_push',
            field=models.ForeignKey(blank=True, help_text='BrewPi Sensors to push (create one push target per sensor to push)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brewfather_push_target2', to='app.BrewPiDevice'),
        ),
        migrations.AddField(
            model_name='brewfatherpushtarget',
            name='device_type',
            field=models.CharField(choices=[('gravity', 'Gravity sensors'), ('brewpi', 'Brewpi sensors')], default='gravity', help_text='What type of device to send', max_length=24),
        ),
        migrations.AlterField(
            model_name='brewfatherpushtarget',
            name='gravity_sensor_to_push',
            field=models.ForeignKey(blank=True, help_text='Gravity Sensor to push (create one push target per sensor to push)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brewfather_push_target', to='gravity.GravitySensor'),
        ),
    ]
