# Generated by Django 4.0.3 on 2022-03-18 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=5, max_digits=20)),
                ('purpose', models.TextField()),
                ('dataTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('took', models.DecimalField(decimal_places=5, max_digits=20)),
                ('gave', models.DecimalField(decimal_places=5, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='took',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=5, max_digits=20)),
                ('purpose', models.TextField()),
                ('dataTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
