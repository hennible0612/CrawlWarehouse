# Generated by Django 3.2.9 on 2021-11-30 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mallboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interpark',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='interpark',
            name='mallName',
            field=models.TextField(default='인터파크', max_length=255),
        ),
    ]
