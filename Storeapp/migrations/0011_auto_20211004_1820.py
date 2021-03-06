# Generated by Django 3.2.6 on 2021-10-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Storeapp', '0010_auto_20210915_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='total_usb_2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Наличие USB 2.0'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='total_usb_3_2_gen1_type_a_5gbit',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Всего USB 3.2 Gen1 Type-A (5 Гбит/с)'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='total_usb_3_2_gen1_type_c_5gbit',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Всего USB 3.2 Gen1 Type-C (5 Гбит/с)'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='total_usb_3_2_gen2_type_c_10gbit',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Всего USB 3.2 Gen2 Type-C (10 Гбит/с)'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='total_usb_3_2_gen2x2_20gbit',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Всего USB 3.2 Gen 2x2 (20 Гбит/с)'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='total_usb_type_a',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Наличие USB Type A'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='total_usb_type_c',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Всего USB Type C'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='usb_3_2_gen1_type_a_10gbit',
            field=models.BooleanField(default=True, verbose_name='Наличие USB 3.2 Gen1 Type-A (10 Гбит/с)'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='usb_3_2_gen1_type_a_5gbit',
            field=models.BooleanField(default=True, verbose_name='Наличие USB 3.2 Gen1 Type-A (5 Гбит/с)'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='usb_3_2_gen1_type_c_5gbit',
            field=models.BooleanField(default=True, verbose_name='Наличие USB 3.2 Gen1 Type-C (5 Гбит/с)'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='usb_3_2_gen2_type_c_10gbit',
            field=models.BooleanField(default=True, verbose_name='Наличие USB 3.2 Gen2 Type-C (10 Гбит/с)'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='usb_3_2_gen2x2_20gbit',
            field=models.BooleanField(default=True, verbose_name='Наличие USB 3.2 Gen 2x2 (20 Гбит/с)'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='usb_4',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Наличие USB4 (до 40 Гбит/с)'),
        ),
    ]
