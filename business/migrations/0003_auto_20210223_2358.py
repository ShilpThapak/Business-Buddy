# Generated by Django 3.1.5 on 2021-02-23 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='employees',
        ),
        migrations.AddField(
            model_name='role',
            name='name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='business.role'),
        ),
    ]