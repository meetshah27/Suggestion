# Generated by Django 4.1.5 on 2023-05-25 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mail', models.CharField(default=None, max_length=50)),
                ('Role', models.CharField(default=None, max_length=50)),
                ('Department', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]