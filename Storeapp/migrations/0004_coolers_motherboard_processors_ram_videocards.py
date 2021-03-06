# Generated by Django 3.2.6 on 2021-09-06 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Storeapp', '0003_tabicons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coolers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, verbose_name='Тип')),
                ('cooling_type', models.CharField(max_length=20, verbose_name='Тип охлаждения')),
                ('socket', models.CharField(max_length=255, verbose_name='Сокет')),
                ('power_dissipation', models.IntegerField(default=0, verbose_name='Рассеиваемая мощность')),
                ('radiator_metal', models.CharField(max_length=20, verbose_name='Материал радиатора')),
                ('heat_pipes', models.BooleanField(default=True, verbose_name='Тепловые трубки')),
                ('total_heat_pipes', models.IntegerField(default=0, verbose_name='Всего тепловых трубок')),
                ('evaporation', models.BooleanField(default=True, verbose_name='Испарительные камеры')),
                ('fan_diameter', models.IntegerField(default=0, verbose_name='Диаметр вентилятора')),
                ('total_fans', models.IntegerField(default=0, verbose_name='Количество вентиляторов')),
                ('bearing', models.CharField(max_length=20, verbose_name='Подшипник')),
                ('max_rotation_speed', models.IntegerField(default=0, verbose_name='Максимальная скорость вращения')),
                ('rotation_speed_control', models.BooleanField(default=True, verbose_name='Контроль скорости вращения (PWM)')),
                ('thermal_control', models.BooleanField(default=True, verbose_name='Термоконтроль')),
                ('connection_type', models.IntegerField(default=0, verbose_name='Тип подключения')),
                ('led', models.BooleanField(default=True, verbose_name='LED-подсветка')),
                ('vibration_isolation', models.BooleanField(default=True, verbose_name='Виброизоляция')),
                ('noise_lvl', models.FloatField(default=0, verbose_name='Уровень шума')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('depth', models.IntegerField(default=0, verbose_name='Глубина')),
                ('height', models.IntegerField(default=0, verbose_name='Высота')),
                ('weight', models.IntegerField(default=0, verbose_name='Вес')),
            ],
            options={
                'verbose_name': 'Оперативная память',
                'verbose_name_plural': 'Оперативная память',
            },
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_launch_date', models.IntegerField(default=0, verbose_name='Дата выхода на рынок')),
                ('processor_support', models.CharField(max_length=20, verbose_name='Поддержка процессоров')),
                ('socket', models.CharField(max_length=20, verbose_name='Сокет')),
                ('chipset', models.CharField(max_length=20, verbose_name='Чипсет')),
                ('form_factor', models.CharField(max_length=20, verbose_name='Форм-фактор')),
                ('backlight', models.BooleanField(default=True, verbose_name='Подсветка')),
                ('memory_type', models.CharField(max_length=20, verbose_name='Тип памяти')),
                ('number_of_memory_slots', models.IntegerField(default=0, verbose_name='Количество слотов памяти')),
                ('max_memory', models.IntegerField(default=0, verbose_name='Максимальный объём памяти')),
                ('memory_mode', models.IntegerField(default=0, verbose_name='Режим памяти')),
                ('max_memory_frequency', models.IntegerField(default=0, verbose_name='Максимальная частота памяти')),
                ('ver_pcl_express', models.CharField(max_length=20, verbose_name='Версия PCI Express')),
                ('pcl_express_x16', models.BooleanField(default=True, verbose_name='PCI Express x16')),
                ('total_pcl_express_x16', models.IntegerField(default=0, verbose_name='Количество PCI Express x16')),
                ('pcl_express_2_x16', models.BooleanField(default=True, verbose_name='PCI Express 2.0 x16')),
                ('total_pcl_express_2_x16', models.IntegerField(default=0, verbose_name='Количество PCI Express 2.0 x16')),
                ('pcl_express_x1', models.BooleanField(default=True, verbose_name='PCI Express x1')),
                ('total_pcl_express_x1', models.IntegerField(default=0, verbose_name='Количество PCI Express x1')),
                ('pcl_express_2_x1', models.BooleanField(default=True, verbose_name='Из них PCI Express 2.0 x1')),
                ('total_pcl_express_2_x1', models.IntegerField(default=0, verbose_name='Количество PCI Express 2.0 x1')),
                ('pcl_express_x4', models.BooleanField(default=True, verbose_name='Из них PCI Express x4')),
                ('total_pcl_express_2_x4', models.IntegerField(default=0, verbose_name='Количество PCI Express 2.0 x4')),
                ('pcl_express_x8', models.BooleanField(default=True, verbose_name='Из них PCI Express x8')),
                ('total_pcl_express_2_x8', models.IntegerField(default=0, verbose_name='Количество PCI Express 2.0 x8')),
                ('pcl', models.BooleanField(default=True, verbose_name='PCI')),
                ('m2', models.BooleanField(default=True, verbose_name='ssd M.2')),
                ('total_m2', models.IntegerField(default=0, verbose_name='Количество ssd M.2')),
                ('sata_3', models.BooleanField(default=True, verbose_name='SATA 3.0')),
                ('total_sata_3', models.IntegerField(default=0, verbose_name='Количество SATA 3.0')),
                ('sata_2', models.BooleanField(default=True, verbose_name='SATA 2.0')),
                ('raid', models.BooleanField(default=True, verbose_name='RAID')),
                ('raid_info', models.CharField(max_length=20, verbose_name='RAID инфо')),
                ('slot_for_wifi_module', models.BooleanField(default=True, verbose_name='Слот для модуля Wi-Fi')),
                ('wifi', models.BooleanField(default=True, verbose_name='Wi-Fi')),
                ('bluetooth', models.BooleanField(default=True, verbose_name='Bluetooth')),
                ('ethernet', models.BooleanField(default=True, verbose_name='Ethernet')),
                ('integrated_graphics_support', models.BooleanField(default=True, verbose_name='Поддержка встроенной графики')),
                ('sli_crossfire_support', models.BooleanField(default=True, verbose_name='Поддержка SLi/CrossFire')),
                ('built_in_sound', models.BooleanField(default=True, verbose_name='Встроенный звук')),
                ('built_in_sound_type', models.CharField(max_length=20, verbose_name='Встроенный звук тип')),
                ('sound_scheme', models.FloatField(default=0, verbose_name='Звуковая схема')),
                ('usb_2', models.BooleanField(default=True, verbose_name='USB 2.0')),
                ('total_usb_2', models.IntegerField(default=0, verbose_name='Количество USB 2.0')),
                ('usb_3_gen1_type_a_5gbit', models.BooleanField(default=True, verbose_name='USB 3.2 Gen1 Type-A (5 Гбит/с)')),
                ('total_usb_3_gen1_type_a_5gbit', models.IntegerField(default=0, verbose_name='Всего USB 3.2 Gen1 Type-A (5 Гбит/с)')),
                ('usb_3_gen2_type_a_10gbit', models.BooleanField(default=True, verbose_name='USB 3.2 Gen2 Type-A (10 Гбит/с)')),
                ('total_usb_3_gen2_type_a_10gbit', models.IntegerField(default=0, verbose_name='Всего USB 3.2 Gen2 Type-A (10 Гбит/с)')),
                ('usb_3_gen1_type_c_5gbit', models.BooleanField(default=True, verbose_name='USB 3.2 Gen1 Type-C (5 Гбит/с)')),
                ('total_usb_3_gen1_type_c_5gbit', models.IntegerField(default=0, verbose_name='Всего USB 3.2 Gen1 Type-C (5 Гбит/с)')),
                ('usb_3_gen2_type_c_10gbit', models.BooleanField(default=True, verbose_name='USB 3.2 Gen2 Type-C (10 Гбит/с)')),
                ('total_usb_3_gen2_type_c_10gbit', models.IntegerField(default=0, verbose_name='Всего USB 3.2 Gen2 Type-C (10 Гбит/с)')),
                ('usb_c_thunderbolt3', models.BooleanField(default=True, verbose_name='USB-C (Thunderbolt 3)')),
                ('s_pdif_digital_output', models.BooleanField(default=True, verbose_name='Цифровой выход S/PDIF')),
                ('audio_jack', models.BooleanField(default=True, verbose_name='Аудио (3.5 мм jack)')),
                ('total_audio_jack', models.IntegerField(default=0, verbose_name='Всего аудио (3.5 мм jack)')),
                ('com', models.BooleanField(default=True, verbose_name='COM')),
                ('lpt', models.BooleanField(default=True, verbose_name='LPT')),
                ('ps_2', models.BooleanField(default=True, verbose_name='PS/2')),
                ('total_ps_2', models.IntegerField(default=0, verbose_name='Всего PS/2')),
                ('display_port', models.BooleanField(default=True, verbose_name='DisplayPort')),
                ('mini_display_port', models.BooleanField(default=True, verbose_name='mini DisplayPort ')),
                ('vga', models.BooleanField(default=True, verbose_name='VGA (D-Sub)')),
                ('dvi', models.BooleanField(default=True, verbose_name='DVI')),
                ('hdmi', models.BooleanField(default=True, verbose_name='HDMI')),
                ('total_hdmi', models.IntegerField(default=0, verbose_name='Всего HDMI')),
                ('cpu_fan_connectors', models.BooleanField(default=True, verbose_name='Разъемы для вентилятора ЦП')),
                ('total_cpu_fan_connectors', models.IntegerField(default=0, verbose_name='Всего разъемов для вентилятора ЦП')),
                ('sockets_for_cbo_processor', models.BooleanField(default=True, verbose_name='Разъемы для СВО процессора')),
                ('total_sockets_for_cbo_processor', models.IntegerField(default=0, verbose_name='Всего разъемов для СВО процессора')),
                ('case_fan_connectors', models.BooleanField(default=True, verbose_name='Разъемы для корпусных вентиляторов')),
                ('total_case_fan_connectors', models.IntegerField(default=0, verbose_name='Всего разъемов для корпусных вентиляторов')),
                ('enable_5v_argb_lighting_connectors', models.BooleanField(default=True, verbose_name='Разъемы для подсветки ARGB 5В')),
                ('total_5v_argb_lighting_connectors', models.IntegerField(default=0, verbose_name='Всего разъемов для подсветки ARGB 5В')),
                ('enable_12v_lighting_connectors', models.BooleanField(default=True, verbose_name='Разъемы для подсветки RGB 12В')),
                ('total_12v_lighting_connectors', models.IntegerField(default=0, verbose_name='Всего разъемов для подсветки RGB 12В')),
            ],
            options={
                'verbose_name': 'Материнская плата',
                'verbose_name_plural': 'Материнские платы',
            },
        ),
        migrations.CreateModel(
            name='Processors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_launch_date', models.IntegerField(default=0, verbose_name='Дата выхода на рынок')),
                ('the_lineup', models.CharField(max_length=20, verbose_name='Модельный ряд')),
                ('delivery_type', models.CharField(max_length=20, verbose_name='Тип поставки')),
                ('cooling_included', models.BooleanField(default=True, verbose_name='Охлаждение в комплекте')),
                ('crystal_code_name', models.CharField(max_length=255, verbose_name='Кодовое название кристалла')),
                ('socket', models.CharField(max_length=20, verbose_name='Сокет')),
                ('number_of_cores', models.IntegerField(default=0, verbose_name='Количество ядер')),
                ('maximum_number_of_threads', models.IntegerField(default=0, verbose_name='Максимальное количество потоков')),
                ('base_clock_frequency', models.FloatField(default=0, verbose_name='Базовая тактовая частота')),
                ('max_frequency', models.FloatField(default=0, verbose_name='Максимальная частота')),
                ('cash_l2', models.IntegerField(default=0, verbose_name='Кэш L2')),
                ('cash_l3', models.IntegerField(default=0, verbose_name='Кэш L3')),
                ('memory_support', models.CharField(max_length=20, verbose_name='Поддержка памяти')),
                ('number_of_memory_channels', models.IntegerField(default=0, verbose_name='Количество каналов памяти')),
                ('max_memory_frequency', models.IntegerField(default=0, verbose_name='Макс. частота памяти')),
                ('integrated_gpu_express_controller', models.BooleanField(default=True, verbose_name='Встроенный контроллер PCI Express')),
                ('type_gpu_express_controller', models.CharField(max_length=20, verbose_name='Тип встроенного контроллера PCI Express')),
                ('integrated_graphics', models.BooleanField(default=True, verbose_name='Встроенная графика')),
                ('tdp', models.IntegerField(default=0, verbose_name='Расчетная тепловая мощность (TDP)')),
                ('technical_process', models.IntegerField(default=0, verbose_name='Техпроцесс')),
                ('kernel_multi_threading', models.BooleanField(default=True, verbose_name='Многопоточность ядра')),
            ],
            options={
                'verbose_name': 'Процессор',
                'verbose_name_plural': 'Процессоры',
            },
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kit', models.IntegerField(default=0, verbose_name='Набор')),
                ('capacity', models.IntegerField(default=0, verbose_name='Объем')),
                ('type', models.CharField(max_length=20, verbose_name='Тип памяти')),
                ('ecc', models.BooleanField(default=True, verbose_name='ECC')),
                ('frequency', models.IntegerField(default=0, verbose_name='Частота')),
                ('pc_index', models.IntegerField(default=0, verbose_name='PC-индекс')),
                ('cas_latency', models.IntegerField(default=0, verbose_name='CAS Latency')),
                ('timings', models.IntegerField(default=0, verbose_name='Тайминги')),
                ('supply_voltage', models.FloatField(default=0, verbose_name='Напряжение питания')),
                ('chip_location', models.CharField(max_length=20, verbose_name='Расположение чипов')),
                ('number_of_ranks', models.IntegerField(default=0, verbose_name='Количество ранков')),
                ('number_of_micro', models.IntegerField(default=0, verbose_name='Число микросхем')),
                ('capacity_of_micro', models.IntegerField(default=0, verbose_name='Ёмкость микросхем')),
                ('micro_type', models.CharField(max_length=20, verbose_name='Тип микросхем')),
                ('xmp_profile', models.BooleanField(default=True, verbose_name='Профили XMP')),
                ('amp_profile', models.BooleanField(default=True, verbose_name='Профили AMP')),
                ('cooling', models.BooleanField(default=True, verbose_name='Охлаждение')),
                ('low_module', models.BooleanField(default=True, verbose_name='Низкопрофильный модуль')),
                ('illumination', models.BooleanField(default=True, verbose_name='Подсветка элементов платы')),
                ('color', models.CharField(max_length=20, verbose_name='Подсветка элементов платы')),
            ],
            options={
                'verbose_name': 'Оперативная память',
                'verbose_name_plural': 'Оперативная память',
            },
        ),
        migrations.CreateModel(
            name='VideoCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interface', models.CharField(max_length=255, verbose_name='Интерфейс')),
                ('gpu_manufacturer', models.CharField(max_length=20, verbose_name='Производитель графического процессора')),
                ('gpu', models.CharField(max_length=20, verbose_name='Графический процессор')),
                ('overclocked_version', models.BooleanField(default=True, verbose_name='Разогнанная версия')),
                ('lhr', models.BooleanField(default=True, verbose_name='Защита от майнинга (LHR)')),
                ('base_gpu_frequency', models.IntegerField(default=0, verbose_name='Базовая частота графического процессора')),
                ('max_gpu_frequency', models.IntegerField(default=0, verbose_name='Максимальная частота графического процессора')),
                ('number_of_stream_processors', models.IntegerField(default=0, verbose_name='Количество потоковых процессоров')),
                ('video_memory', models.IntegerField(default=0, verbose_name='Видеопамять')),
                ('type_video_memory', models.CharField(max_length=20, verbose_name='Тип видеопамяти')),
                ('effective_memory_frequency', models.IntegerField(default=0, verbose_name='Эффективная частота памяти')),
                ('memory_bandwidth', models.IntegerField(default=0, verbose_name='Пропускная способность памяти')),
                ('memory_bus_width', models.IntegerField(default=0, verbose_name='Ширина шины памяти')),
                ('directx_support', models.IntegerField(default=0, verbose_name='Поддержка DirectX')),
                ('sli_crossfire_support', models.BooleanField(default=True, verbose_name='Поддержка SLI/CrossFire')),
                ('power_connectors', models.IntegerField(default=0, verbose_name='Разъемы питания')),
                ('recommended_power_supply', models.IntegerField(default=0, verbose_name='Рекомендуемый блок питания')),
                ('air_cooling', models.BooleanField(default=True, verbose_name='Охлаждение воздушное')),
                ('water_cooling', models.BooleanField(default=True, verbose_name='Охлаждение жидкостное')),
                ('cooling_system_thickness', models.IntegerField(default=0, verbose_name='Толщина системы охлаждения')),
                ('card_length', models.IntegerField(default=0, verbose_name='Длина видеокарты')),
                ('card_height', models.IntegerField(default=0, verbose_name='Высота видеокарты ')),
                ('vga', models.BooleanField(default=True, verbose_name='VGA')),
                ('dvi', models.BooleanField(default=True, verbose_name='DVI')),
                ('hdmi', models.BooleanField(default=True, verbose_name='HDMI')),
                ('mini_hdmi', models.BooleanField(default=True, verbose_name='mini HDMI')),
                ('display_port', models.BooleanField(default=True, verbose_name='DisplayPort')),
                ('mini_display_port', models.BooleanField(default=True, verbose_name='mini Display Port')),
                ('vesa_stereo', models.BooleanField(default=True, verbose_name='VESA Stereo')),
                ('usb_type_c', models.BooleanField(default=True, verbose_name='USB Type-C ')),
            ],
            options={
                'verbose_name': 'Видеокартa',
                'verbose_name_plural': 'Видеокарты',
            },
        ),
    ]
