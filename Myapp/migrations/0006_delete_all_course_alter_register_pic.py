# Generated by Django 4.0.2 on 2022-03-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0005_alter_register_pic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='All_Course',
        ),
        migrations.AlterField(
            model_name='register',
            name='pic',
            field=models.ImageField(default='logo6.png', upload_to='Profile Pic'),
        ),
    ]