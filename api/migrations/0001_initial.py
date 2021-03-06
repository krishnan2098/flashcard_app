# Generated by Django 4.0 on 2022-01-03 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=20)),
                ('audio', models.TextField(blank=True, null=True)),
                ('is_completed', models.BooleanField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meaning', models.TextField(blank=True, null=True)),
                ('part_of_speech', models.CharField(max_length=20)),
                ('example', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meanings', to='api.flashcard')),
            ],
        ),
    ]
