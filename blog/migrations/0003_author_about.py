# Generated by Django 4.2.3 on 2023-07-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='about',
            field=models.CharField(max_length=600, null=True),
        ),
    ]