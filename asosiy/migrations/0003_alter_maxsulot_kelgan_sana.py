# Generated by Django 4.1.1 on 2022-09-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0002_alter_maxsulot_olchov'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maxsulot',
            name='kelgan_sana',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]