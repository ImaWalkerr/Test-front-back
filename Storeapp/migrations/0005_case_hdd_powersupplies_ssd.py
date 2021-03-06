# Generated by Django 3.2.6 on 2021-09-07 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Storeapp', '0004_coolers_motherboard_processors_ram_videocards'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power_supply', models.CharField(max_length=20, verbose_name='Блок питания')),
                ('type_of_case', models.CharField(max_length=20, verbose_name='Тип корпуса')),
                ('game_type', models.BooleanField(default=True, verbose_name='Игровой корпус')),
                ('case_color', models.CharField(max_length=20, verbose_name='Цвет корпуса')),
                ('case_material', models.CharField(max_length=20, verbose_name='Материал корпуса')),
                ('window_material', models.CharField(max_length=20, verbose_name='Материал окна')),
                ('max_motherboard_size', models.CharField(max_length=20, verbose_name='Макс.размер материнской платы')),
                ('compatible_motherboard', models.CharField(max_length=20, verbose_name='Совместимые материнские платы')),
                ('power_supply_loc', models.CharField(max_length=20, verbose_name='Расположение блока питания')),
                ('fans_included', models.BooleanField(default=True, verbose_name='Вентиляторы в комплекте')),
                ('liquid_cooling_support', models.BooleanField(default=True, verbose_name='Поддержка жидкостного охлаждения')),
                ('number_of_places_for_fans', models.IntegerField(default=0, verbose_name='Количество мест для вентиляторов')),
                ('installed_coolers', models.IntegerField(default=0, verbose_name='Установленные кулеры')),
                ('cooler_illumination_color', models.CharField(max_length=20, verbose_name='Цвет подсветки кулера')),
                ('noise_isolation', models.BooleanField(default=True, verbose_name='Шумоизоляция')),
                ('bays_5_inches', models.BooleanField(default=True, verbose_name='Отсеки 5.25 дюймов')),
                ('external_bays_inches', models.BooleanField(default=True, verbose_name='Внешние отсеки 3.5 дюймов')),
                ('internal_bays_inches', models.BooleanField(default=True, verbose_name='Внутренние отсеки 3.5 дюймов')),
                ('bays_2_inches', models.BooleanField(default=True, verbose_name='Отсеки 2.5 дюймов')),
                ('remove_hard_drive_cage', models.BooleanField(default=True, verbose_name='Съёмная корзина жестких дисков')),
                ('screwless_drive_mounting', models.BooleanField(default=True, verbose_name='Безвинтовое крепление дисков')),
                ('expansion_slots', models.IntegerField(default=0, verbose_name='Слоты расширения')),
                ('dust_filters', models.BooleanField(default=True, verbose_name='Пылевые фильтры')),
                ('transparent_window', models.BooleanField(default=True, verbose_name='Прозрачное окно')),
                ('backlight_housing', models.BooleanField(default=True, verbose_name='Подсветка корпуса')),
                ('fan_rotation_controller', models.BooleanField(default=True, verbose_name='Контроллер вращения вентиляторов')),
                ('max_video_card_length', models.IntegerField(default=0, verbose_name='Макс.длина видеокарты')),
                ('max_cpu_cooler_height', models.IntegerField(default=0, verbose_name='Макс.высота процессорного кулера')),
                ('door', models.BooleanField(default=True, verbose_name='Дверца')),
                ('lock', models.BooleanField(default=True, verbose_name='Замок')),
                ('info_display', models.BooleanField(default=True, verbose_name='Информационный дисплей')),
                ('usb_2', models.BooleanField(default=True, verbose_name='USB 2.0')),
                ('usb_3_gen1_type_a_5gbit', models.BooleanField(default=True, verbose_name='USB 3.2 Gen1 Type-A (5 Гбит/с)')),
                ('usb_3_gen1_type_c_5gbit', models.BooleanField(default=True, verbose_name='USB 3.2 Gen1 Type-C (5 Гбит/с)')),
                ('firewire', models.BooleanField(default=True, verbose_name='FireWire (IEEE 1394, iLink)')),
                ('esata', models.BooleanField(default=True, verbose_name='eSATA')),
                ('hard_drive_docking_station', models.BooleanField(default=True, verbose_name='Док-станция для винчестеров')),
                ('cardreader', models.BooleanField(default=True, verbose_name='Кардридер')),
                ('audio_output', models.BooleanField(default=True, verbose_name='Аудио выход')),
                ('micro_output', models.BooleanField(default=True, verbose_name='Вход для микрофона')),
                ('height', models.IntegerField(default=0, verbose_name='Высота')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('depth', models.IntegerField(default=0, verbose_name='Глубина')),
                ('weight', models.FloatField(default=0, verbose_name='Вес')),
            ],
            options={
                'verbose_name': 'Корпус',
                'verbose_name_plural': 'Корпуса',
            },
        ),
        migrations.CreateModel(
            name='HDD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drive_type', models.CharField(max_length=20, verbose_name='Тип накопителя')),
                ('capacity', models.IntegerField(default=0, verbose_name='Объём')),
                ('form_factor', models.FloatField(default=0, verbose_name='Форм-фактор')),
                ('interface', models.CharField(max_length=20, verbose_name='Интерфейс')),
                ('spindle_speed', models.IntegerField(default=0, verbose_name='Скорость вращения шпинделя')),
                ('buffer', models.IntegerField(default=0, verbose_name='Буфер')),
                ('sector_size', models.IntegerField(default=0, verbose_name='Размер сектора')),
                ('power_consumption_1', models.FloatField(default=0, verbose_name='Энергопотребление (чтение/запись)')),
                ('power_consumption_2', models.FloatField(default=0, verbose_name='Энергопотребление (ожидание)')),
                ('time_between_failures', models.IntegerField(default=0, verbose_name='Время наработки на отказ (МТBF)')),
                ('thickness', models.FloatField(default=0, verbose_name='Толщина')),
            ],
            options={
                'verbose_name': 'HDD',
                'verbose_name_plural': 'HDD',
            },
        ),
        migrations.CreateModel(
            name='PowerSupplies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment', models.CharField(max_length=20, verbose_name='Назначение')),
                ('power', models.IntegerField(default=0, verbose_name='Мощность')),
                ('power_supply_standard', models.CharField(max_length=20, verbose_name='Стандарт блока питания')),
                ('number_of_separate_lines_12v', models.IntegerField(default=0, verbose_name='Количество отдельных линий +12V')),
                ('max_line_current_12v', models.IntegerField(default=0, verbose_name='Макс. ток по линии +12V')),
                ('combined_load_12v', models.IntegerField(default=0, verbose_name='Комбинированная нагрузка по +12V')),
                ('power_factor_correction', models.BooleanField(default=0, verbose_name='Коррекция фактора мощности (PFC)')),
                ('efficiency', models.IntegerField(default=0, verbose_name='КПД')),
                ('certificate_80_plus', models.BooleanField(default=True, verbose_name='Сертификат 80 PLUS')),
                ('power_supply_fan_size', models.IntegerField(default=0, verbose_name='Размер вентилятора блока питания')),
                ('total_fans', models.IntegerField(default=0, verbose_name='Количество вентиляторов')),
                ('fan_illumination', models.BooleanField(default=True, verbose_name='Подсветка вентилятора')),
                ('power_cable_length', models.FloatField(default=0, verbose_name='Длина кабеля питания')),
                ('modular_power_cable_connection', models.BooleanField(default=True, verbose_name='Модульное подключение кабелей питания')),
                ('motherboard_power', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Питание материнской платы')),
                ('cpu_4_pin', models.BooleanField(default=True, verbose_name='CPU 4 pin')),
                ('cpu_8_pin', models.BooleanField(default=True, verbose_name='CPU 8 pin')),
                ('fdd_4_pin', models.BooleanField(default=True, verbose_name='FDD 4 pin')),
                ('ide_4_pin', models.BooleanField(default=True, verbose_name='IDE 4 pin')),
                ('sata', models.BooleanField(default=True, verbose_name='SATA')),
                ('pcle_6_pin', models.BooleanField(default=True, verbose_name='PCIe 6 pin')),
                ('pcle_8_pin', models.BooleanField(default=True, verbose_name='PCIe 8 pin')),
                ('usb_power', models.BooleanField(default=True, verbose_name='USB Power')),
                ('height', models.IntegerField(default=0, verbose_name='Высота')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('depth', models.IntegerField(default=0, verbose_name='Глубина')),
            ],
            options={
                'verbose_name': 'Блок питания',
                'verbose_name_plural': 'Блоки питания',
            },
        ),
        migrations.CreateModel(
            name='SSD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_launch_date', models.IntegerField(default=0, verbose_name='Дата выхода на рынок')),
                ('capacity', models.IntegerField(default=0, verbose_name='Объём')),
                ('form_factor', models.FloatField(default=0, verbose_name='Форм-фактор')),
                ('interface', models.CharField(max_length=20, verbose_name='Интерфейс')),
                ('chip_type_flash', models.CharField(max_length=255, verbose_name='Тип микросхем Flash')),
                ('hardware_encryption', models.BooleanField(default=True, verbose_name='Аппаратное шифрование')),
                ('thickness', models.IntegerField(default=0, verbose_name='Толщина')),
                ('cooling', models.BooleanField(default=True, verbose_name='Охлаждение')),
                ('backlight', models.BooleanField(default=True, verbose_name='Подсветка')),
                ('adapter', models.BooleanField(default=True, verbose_name='Адаптер 3.5')),
            ],
            options={
                'verbose_name': 'SSD',
                'verbose_name_plural': 'SSD',
            },
        ),
    ]
