# Generated by Django 3.2 on 2021-08-10 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mandalart', '0005_auto_20210809_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='block', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Spelist',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('block', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mandalart.block')),
            ],
        ),
        migrations.CreateModel(
            name='Spelist_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spegoal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mandalart.specificgoal')),
                ('spelist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mandalart.spelist')),
            ],
        ),
    ]
