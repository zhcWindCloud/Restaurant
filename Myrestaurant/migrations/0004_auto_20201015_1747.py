# Generated by Django 2.2 on 2020-10-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myrestaurant', '0003_auto_20201014_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumodels',
            name='MenuCore',
            field=models.CharField(blank=True, default='2.2', max_length=20, null=True, verbose_name='评分'),
        ),
        migrations.AlterField(
            model_name='menumodels',
            name='MenuFree',
            field=models.CharField(blank=True, default='10.7', max_length=20, null=True, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='menumodels',
            name='MenuShell',
            field=models.CharField(blank=True, default='540', max_length=20, null=True, verbose_name='月销售量'),
        ),
    ]