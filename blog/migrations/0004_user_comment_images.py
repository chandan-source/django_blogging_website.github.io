# Generated by Django 3.1 on 2021-12-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211230_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_comment',
            name='images',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
