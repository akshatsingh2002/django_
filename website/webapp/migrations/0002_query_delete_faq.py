# Generated by Django 4.0.6 on 2022-10-15 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('Msg', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='faq',
        ),
    ]
