# Generated by Django 4.1.9 on 2023-05-26 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_alter_comment_user_alter_favorate_user_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='img',
            field=models.ImageField(null=True, upload_to='chapter/'),
        ),
    ]
