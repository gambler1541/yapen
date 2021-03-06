# Generated by Django 2.1 on 2018-08-03 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pensionlike',
            name='pension',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Pension'),
        ),
        migrations.AddField(
            model_name='pensionlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pensionimage',
            name='pension',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Pension'),
        ),
        migrations.AddField(
            model_name='comment',
            name='pension',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location.Pension'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
