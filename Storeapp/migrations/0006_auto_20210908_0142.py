# Generated by Django 3.2.6 on 2021-09-07 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Storeapp', '0005_case_hdd_powersupplies_ssd'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Storeapp.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='description',
            field=models.TextField(max_length=5000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='case',
            name='image',
            field=models.ImageField(default=1, upload_to='web_media/products/', verbose_name='Изображение товара'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Наименование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coolers',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Storeapp.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coolers',
            name='description',
            field=models.TextField(max_length=5000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='coolers',
            name='image',
            field=models.ImageField(default=1, upload_to='web_media/products/', verbose_name='Изображение товара'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coolers',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coolers',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coolers',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Наименование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hdd',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Storeapp.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hdd',
            name='description',
            field=models.TextField(max_length=5000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='hdd',
            name='image',
            field=models.ImageField(default=1, upload_to='web_media/products/', verbose_name='Изображение товара'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hdd',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hdd',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hdd',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Наименование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='motherboard',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Storeapp.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='motherboard',
            name='description',
            field=models.TextField(max_length=5000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='image',
            field=models.ImageField(default=1, upload_to='web_media/products/', verbose_name='Изображение товара'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='motherboard',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='motherboard',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='motherboard',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Наименование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='powersupplies',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Storeapp.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='powersupplies',
            name='description',
            field=models.TextField(max_length=5000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='powersupplies',
            name='image',
            field=models.ImageField(default=1, upload_to='web_media/products/', verbose_name='Изображение товара'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='powersupplies',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='powersupplies',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='powersupplies',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Наименование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processors',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Storeapp.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processors',
            name='description',
            field=models.TextField(max_length=5000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='processors',
            name='image',
            field=models.ImageField(default=1, upload_to='web_media/products/', verbose_name='Изображение товара'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processors',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processors',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processors',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Наименование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ram',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Storeapp.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ram',
            name='description',
            field=models.TextField(max_length=5000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='ram',
            name='image',
            field=models.ImageField(default=1, upload_to='web_media/products/', verbose_name='Изображение товара'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ram',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ram',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ram',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Наименование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ssd',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Storeapp.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ssd',
            name='description',
            field=models.TextField(max_length=5000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='ssd',
            name='image',
            field=models.ImageField(default=1, upload_to='web_media/products/', verbose_name='Изображение товара'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ssd',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ssd',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ssd',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Наименование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videocards',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Storeapp.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videocards',
            name='description',
            field=models.TextField(max_length=5000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='videocards',
            name='image',
            field=models.ImageField(default=1, upload_to='web_media/products/', verbose_name='Изображение товара'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videocards',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videocards',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videocards',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Наименование'),
            preserve_default=False,
        ),
    ]