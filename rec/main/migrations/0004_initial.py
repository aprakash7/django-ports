# Generated by Django 4.0.5 on 2022-06-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0003_delete_commands'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outputs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op', models.CharField(max_length=800)),
            ],
        ),
    ]
