# Generated by Django 2.2.14 on 2022-11-03 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_userprofile_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Item',
            field=models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Item'),
        ),
    ]
