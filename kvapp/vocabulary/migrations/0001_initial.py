# Generated by Django 5.1.4 on 2025-01-03 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korean_word', models.CharField(max_length=100)),
                ('english_translation', models.CharField(max_length=200)),
                ('example_sentence', models.TextField(blank=True)),
            ],
        ),
    ]