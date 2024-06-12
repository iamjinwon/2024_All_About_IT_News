# Generated by Django 4.2.13 on 2024-06-12 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0003_alter_user_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gpt',
            fields=[
                ('news', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='newApp.news')),
                ('input_tokens', models.IntegerField()),
                ('output_tokens', models.IntegerField()),
                ('total_tokens', models.IntegerField()),
                ('cost', models.FloatField()),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Gpt',
                'managed': True,
            },
        ),
    ]
