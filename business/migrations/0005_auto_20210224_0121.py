# Generated by Django 3.1.5 on 2021-02-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20210224_0116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='Assignedto',
            new_name='assignedto',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='Interest',
        ),
        migrations.AddField(
            model_name='lead',
            name='interest',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='stage',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]