# Generated by Django 2.2.2 on 2019-06-22 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketslot',
            name='add_datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='время создания'),
        ),
        migrations.AlterField(
            model_name='basketslot',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='количество'),
        ),
        migrations.AlterField(
            model_name='basketslot',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to=settings.AUTH_USER_MODEL),
        ),
    ]