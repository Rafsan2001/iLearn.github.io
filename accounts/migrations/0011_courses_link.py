# Generated by Django 3.2.5 on 2021-09-12 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='link',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
