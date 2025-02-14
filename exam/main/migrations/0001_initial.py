# Generated by Django 4.2.11 on 2024-07-03 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.CharField(max_length=9)),
                ('description', models.TextField()),
                ('stat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.stat', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ['numbers'],
            },
        ),
    ]
