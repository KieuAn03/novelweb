# Generated by Django 4.1.9 on 2023-05-26 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_user_rename_truyen_truyen_category_truyen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user'),
        ),
        migrations.AlterField(
            model_name='favorate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user'),
        ),
    ]
