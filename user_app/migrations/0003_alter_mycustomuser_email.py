# Generated by Django 4.1.3 on 2023-08-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_alter_mycustomuser_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycustomuser',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
