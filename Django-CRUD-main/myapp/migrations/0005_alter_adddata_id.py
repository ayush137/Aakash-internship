# Generated by Django 3.2.3 on 2021-06-11 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_adddata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
