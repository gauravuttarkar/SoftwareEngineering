# Generated by Django 2.0.9 on 2019-04-07 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0008_auto_20190407_1227'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(default=None, max_length=20, null=True)),
                ('bankDetails', models.CharField(default=None, max_length=20, null=True)),
                ('comments', models.CharField(default=None, max_length=50, null=True)),
                ('eventId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('userName', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
