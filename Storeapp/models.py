from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse


User = get_user_model()


def get_models_for_count(*model_names):
    return [models.Count(model_name) for model_name in model_names]


def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class MinResolutionErrorException(Exception):
    pass


class MaxResolutionErrorException(Exception):
    pass


class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True
                    )
        return products


class LatestProducts:

    objects = LatestProductsManager()


class CategoryManager(models.Manager):

    CATEGORY_NAME_COUNT_NAME = {
        'Ноутбуки': 'notebook__count',
        'Смартфоны': 'smartphone__count',
        'Видеокарты': 'videocards__count',
        'Процессоры': 'processors__count',
        'Материнские платы': 'motherboards__count',
        'Оперативная память': 'ram__count',
        'Кулеры': 'coolers__count',
        'SSD': 'ssd__count',
        'HDD': 'hdd__count',
        'Корпуса': 'case__count',
        'Блоки питания': 'powersupply__count'
    }

    def get_queryset(self):
        return super().get_queryset()

    def get_categories_for_left_sidebar(self):
        models = get_models_for_count(
            'notebook', 'smartphone', 'videocards', 'processors', 'motherboard', 'ram', 'coolers', 'ssd', 'hdd',
            'case', 'powersupply'
        )
        qs = list(self.get_queryset().annotate(*models))
        data = [
            dict(name=c.name, url=c.get_absolute_url(), count=getattr(c, self.CATEGORY_NAME_COUNT_NAME[c.name]))
            for c in qs
        ]
        return data


class Category(models.Model):
    """Категории"""
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    company = models.CharField(max_length=255, verbose_name='Компания-производитель')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение товара', upload_to='web_media/products/')
    description = models.TextField(max_length=5000, null=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title


class Notebook(Product):
    """Ноутбуки"""
    date = models.CharField(max_length=255, verbose_name='Дата выхода на рынок')
    product_line = models.CharField(max_length=255, verbose_name='Продуктовая линейка')
    type = models.CharField(max_length=255, verbose_name='Тип ноутбука')
    platform_codename = models.CharField(max_length=255, verbose_name='Платформа(кодовое название)')
    processor_model = models.CharField(max_length=255, verbose_name='Модель процессора')
    number_of_cores_cpu = models.CharField(max_length=255, verbose_name='Количество ядер процессора')
    number_of_threads_cpu = models.CharField(max_length=255, verbose_name='Количество потоков процессора')
    clock_frequency_cpu = models.CharField(max_length=255, verbose_name='Тактовая частота процессора')
    turbo_frequency_cpu = models.CharField(max_length=255, verbose_name='Турбо частота процессора')
    cpu_power_consumption = models.CharField(max_length=255, verbose_name='Энергопотребление процессора')
    cpu_graphics = models.CharField(max_length=255, verbose_name='Встроенная графика')
    case_material = models.CharField(max_length=255, verbose_name='Материал корпуса')
    case_color = models.CharField(max_length=255, verbose_name='Цвет корпуса')
    cover_material = models.CharField(max_length=255, verbose_name='Материал крышки')
    cover_color = models.CharField(max_length=255, verbose_name='Цвет крышки')
    case_backlight = models.BooleanField(default=True, verbose_name='Подсветка корпуса')
    protected_case = models.BooleanField(default=True, verbose_name='Защищенный корпус')
    length = models.CharField(max_length=255, verbose_name='Длина')
    width = models.CharField(max_length=255, verbose_name='Ширина')
    thickness = models.CharField(max_length=255, verbose_name='Толщина')
    height = models.CharField(max_length=255, verbose_name='Вес')
    screen_diagonal = models.CharField(max_length=255, verbose_name='Диагональ экрана')
    screen_resolution = models.CharField(max_length=255, verbose_name='Разрешение экрана')
    matrix_frequency = models.CharField(max_length=255, verbose_name='Частота матрицы')
    screen_technology = models.CharField(max_length=255, verbose_name='Технология экрана')
    screen_surface = models.CharField(max_length=255, verbose_name='Поверхность экрана')
    screen_support = models.BooleanField(default=True, verbose_name='Поддержка активного пера')
    screen_protection = models.BooleanField(default=True, verbose_name='Защита от царапин')
    screen_info = models.CharField(max_length=255, verbose_name='Характеристики дисплея')
    ram_type = models.CharField(max_length=255, verbose_name='Тип оперативной памяти')
    ram_frequency = models.CharField(max_length=255, verbose_name='Частота оперативной памяти')
    ram_memory = models.CharField(max_length=255, verbose_name='Объём оперативной памяти')
    max_ram_memory = models.CharField(max_length=255, verbose_name='Максимальный объём оперативной памяти')
    memory_slots = models.IntegerField(default=1, verbose_name='Всего слотов памяти')
    free_memory_slots = models.IntegerField(default=1, verbose_name='Свободных слотов памяти')
    configuration_drive_type = models.CharField(max_length=255, verbose_name='Конфигурация накопителя')
    drive_type = models.CharField(max_length=255, verbose_name='Тип накопителя')
    drive_capacity = models.CharField(max_length=255, verbose_name='Ёмкость накопителя')
    number_of_ssd_slots = models.IntegerField(default=1, verbose_name='Количество слотов для SSD')
    interface_ssd = models.CharField(max_length=255, verbose_name='Интерфейс установленного SSD')
    optical_drive_unit = models.BooleanField(default=True, verbose_name='Оптический привод (ODD)')
    memory_cards = models.BooleanField(default=True, verbose_name='Карты памяти')
    discrete_graphics = models.BooleanField(default=True, verbose_name='Дискретная видеокарта')
    graphics_card_model = models.CharField(max_length=255, verbose_name='Модель видеокарты')
    local_video_memory = models.CharField(max_length=255, verbose_name='Локальная видеопамять')
    graphics_card_feature = models.CharField(max_length=255, verbose_name='Характеристики видеокарты')
    additional_graphics_card_feature = models.CharField(
        max_length=255, verbose_name='Дополнительные характеристики видеокарты'
    )
    camera = models.BooleanField(default=True, verbose_name='Камера')
    built_in_microphone = models.CharField(max_length=255, verbose_name='Встроенный микрофон')
    built_in_speakers = models.CharField(max_length=255, verbose_name='Встроенные динамики')
    numpad = models.BooleanField(default=True, verbose_name='Цифровое поле (Numpad)')
    backlit_keyboard = models.CharField(max_length=255, verbose_name='Подсветка клавиатуры')
    factory_cyrillic_on_keys = models.BooleanField(default=True, verbose_name='Заводская «кириллица» на клавишах')
    cursor_control = models.CharField(max_length=255, verbose_name='Управление курсором')
    multimedia_touchpad = models.BooleanField(default=True, verbose_name='Мультимедийная сенсорная панель')
    privacy_protection_features = models.BooleanField(default=True, verbose_name='Функции защиты приватности')
    nfs = models.CharField(max_length=255, verbose_name='NFC')
    bluetooth = models.CharField(max_length=255, verbose_name='Bluetooth')
    lan = models.CharField(max_length=255, verbose_name='LAN')
    wifi = models.CharField(max_length=255, verbose_name='Wi-Fi')
    mobile = models.BooleanField(default=True, verbose_name='Сотовая связь')
    usb_2 = models.BooleanField(default=True, verbose_name='USB 2.0')
    total_usb_2 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Наличие USB 2.0')
    total_usb_type_a = models.CharField(max_length=255, null=True, blank=True, verbose_name='Наличие USB Type A')
    usb_3_2_gen1_type_a_5gbit = models.BooleanField(
        default=True, verbose_name='Наличие USB 3.2 Gen1 Type-A (5 Гбит/с)'
    )
    total_usb_3_2_gen1_type_a_5gbit = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Всего USB 3.2 Gen1 Type-A (5 Гбит/с)'
    )
    usb_3_2_gen1_type_a_10gbit = models.BooleanField(
        default=True, verbose_name='Наличие USB 3.2 Gen1 Type-A (10 Гбит/с)'
    )
    total_usb_type_c = models.CharField(max_length=255, null=True, blank=True, verbose_name='Всего USB Type C')
    usb_3_2_gen1_type_c_5gbit = models.BooleanField(
        default=True, verbose_name='Наличие USB 3.2 Gen1 Type-C (5 Гбит/с)'
    )
    total_usb_3_2_gen1_type_c_5gbit = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Всего USB 3.2 Gen1 Type-C (5 Гбит/с)'
    )
    usb_3_2_gen2_type_c_10gbit = models.BooleanField(
        default=True, verbose_name='Наличие USB 3.2 Gen2 Type-C (10 Гбит/с)'
    )
    total_usb_3_2_gen2_type_c_10gbit = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Всего USB 3.2 Gen2 Type-C (10 Гбит/с)'
    )
    usb_3_2_gen2x2_20gbit = models.BooleanField(default=True, verbose_name='Наличие USB 3.2 Gen 2x2 (20 Гбит/с)')
    total_usb_3_2_gen2x2_20gbit = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Всего USB 3.2 Gen 2x2 (20 Гбит/с)'
    )
    usb_4 = models.CharField(max_length=255, null=True, blank=True, verbose_name='Наличие USB4 (до 40 Гбит/с)')
    max_usb_speed = models.CharField(max_length=255, verbose_name='Максимальная скорость передачи данных USB')
    alternative_modes_usb_type_c = models.CharField(max_length=255, verbose_name='Альтернативные режимы USB Type C')
    vga = models.BooleanField(default=True, verbose_name='VGA (RGB)')
    hdmi = models.CharField(max_length=255, verbose_name='HDMI')
    mini_display_port = models.BooleanField(default=True, verbose_name='Mini display port')
    audio_outputs = models.BooleanField(default=True, verbose_name='Аудио выходы(3.5мм jack)')
    battery_cells = models.IntegerField(default=1, verbose_name='Количество ячеек аккумулятора')
    energy_reserve = models.CharField(max_length=255, verbose_name='Запас энергии')
    charge_via_usb_type_c = models.BooleanField(default=True, verbose_name='Зарядка ноутбука через USB Type C')
    usb_c_power_adapter = models.BooleanField(default=True, verbose_name='Адаптер питания USB Type C')
    operation_system = models.CharField(max_length=255, verbose_name='Операционная система')
    additional_equipment = models.CharField(max_length=255, verbose_name='Дополнительная комплектация')
    language = models.CharField(max_length=2, verbose_name='Выбор языка')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'


class Smartphone(Product):
    """Смартфоны"""
    date = models.CharField(max_length=255, verbose_name='Дата выхода на рынок')
    mobile_operation_system = models.CharField(max_length=255, verbose_name='Операционная система')
    ver_mobile_operation_system = models.CharField(max_length=255, verbose_name='Версия операционной системы')
    screen_size = models.CharField(max_length=255, verbose_name='Размер экрана')
    screen_resolution_mobile = models.CharField(max_length=255, verbose_name='Разрешение экрана')
    ram_mobile = models.CharField(max_length=255, verbose_name='Оперативная память')
    flash_memory = models.CharField(max_length=255, verbose_name='Флэш-память')
    built_in_camera = models.CharField(max_length=255, verbose_name='Встроенная камера')
    num_of_main_cam = models.CharField(max_length=255, verbose_name='Количество основных камер')
    num_of_matrix_points = models.CharField(max_length=255, verbose_name='Количество точек матрицы')
    num_of_sim_cards = models.CharField(max_length=255, verbose_name='Количество SIM-карт')
    sim_card_format = models.CharField(max_length=255, verbose_name='Формат SIM-карт')
    max_video_resolution = models.CharField(max_length=255, verbose_name='Максимальное разрешение видео')
    memory_card_support = models.CharField(max_length=255, verbose_name='Поддержка карт памяти')
    platform = models.CharField(max_length=255, verbose_name='Платформа')
    cpu = models.CharField(max_length=255, verbose_name='Процессор')
    cpu_clock_speed = models.CharField(max_length=255, verbose_name='Тактовая частота процессора')
    num_of_cores = models.CharField(max_length=255, verbose_name='Кол-во ядер')
    microarchitecture_cpu = models.CharField(max_length=255, verbose_name='Микроархитектура процессора')
    cpu_size = models.CharField(max_length=255, verbose_name='Разрядность процессора')
    technical_process = models.CharField(max_length=255, verbose_name='Техпроцесс')
    graphics_accelerator = models.CharField(max_length=255, verbose_name='Графический ускоритель')
    gpu_frequency = models.CharField(max_length=255, verbose_name='Частота ГПУ')
    body_design = models.CharField(max_length=255, verbose_name='Конструкция корпуса')
    replaceable_panels = models.BooleanField(default=True, verbose_name='Сменные панели')
    body_material = models.CharField(max_length=255, verbose_name='Материал корпуса')
    back_cover_material = models.CharField(max_length=255, verbose_name='Материал задней крышки')
    body_color = models.CharField(max_length=255, verbose_name='Цвет корпуса')
    front_panel_color = models.CharField(max_length=255, verbose_name='Цвет фронтальной панели')
    shockproof_housing = models.BooleanField(default=True, verbose_name='Ударопрочный корпус')
    protection = models.BooleanField(default=True, verbose_name='Пыле- и влагозащита')
    physical_qwerty_keyboard = models.BooleanField(default=True, verbose_name='Физическая QWERTY-клавиатура')
    front_camera_location = models.CharField(max_length=255, verbose_name='Расположение фронтальной камеры')
    fingerprint_scanner_location = models.CharField(
        max_length=255, verbose_name='Расположение сканера отпечатка пальца'
    )
    button_sos = models.CharField(max_length=255, verbose_name='Кнопка SOS')
    length = models.CharField(max_length=255, verbose_name='Длина')
    width = models.CharField(max_length=255, verbose_name='Ширина')
    thickness = models.CharField(max_length=255, verbose_name='Толщина')
    height = models.CharField(max_length=255, verbose_name='Вес')
    screen_technology = models.CharField(max_length=255, verbose_name='Технология экрана')
    num_of_screen_colors = models.CharField(max_length=255, verbose_name='Кол-во цветов экрана')
    screen_res = models.CharField(max_length=255, verbose_name='Разрешающая способность экрана')
    aspect_ratio = models.CharField(max_length=255, verbose_name='Соотношение сторон')
    refresh_rate = models.CharField(max_length=255, verbose_name='Частота обновления экрана')
    touch_screen = models.BooleanField(default=True, verbose_name='Сенсорный экран')
    scratch_protection = models.CharField(max_length=255, verbose_name='Защита от царапин')
    sec_screen_technology = models.CharField(max_length=255, verbose_name='Технология дополнительного экрана')
    camera_specifications = models.CharField(max_length=255, verbose_name='Характеристики камеры')
    additional_camera_modules = models.CharField(max_length=255, verbose_name='Дополнительные модули камеры')
    built_in_flash_main_camera = models.BooleanField(default=True, verbose_name='Встроенная вспышка')
    auto_focus_main_camera = models.BooleanField(default=True, verbose_name='Автоматическая фокусировка')
    optical_stabilization_main_camera = models.BooleanField(default=True, verbose_name='Оптическая стабилизация')
    diaphragm_main_camera = models.CharField(max_length=255, verbose_name='Диафрагма')
    max_frames_per_second_main_camera = models.CharField(max_length=255,
                                                         verbose_name='Максимальное во-во кадров в секунду')
    front_camera = models.CharField(max_length=255, verbose_name='Фронтальная камера')
    dual_camera = models.BooleanField(default=True, verbose_name='Двойная камера')
    auto_focus_front_camera = models.BooleanField(default=True, verbose_name='Автоматическая фокусировка')
    optical_stabilization_front_camera = models.BooleanField(default=True, verbose_name='Оптическая стабилизация')
    built_in_flash_front_camera = models.BooleanField(default=True, verbose_name='Встроенная вспышка')
    diaphragm_front_camera = models.CharField(max_length=255, verbose_name='Диафрагма')
    max_frames_per_second_front_camera = models.CharField(max_length=255,
                                                          verbose_name='Максимальное во-во кадров в секунду')
    stereo_speakers = models.BooleanField(default=True, verbose_name='Стереодинамики')
    fingerprint_scanner = models.BooleanField(default=True, verbose_name='Сканер отпечатка пальца')
    face_or_iris_map_scanner = models.BooleanField(default=True, verbose_name='Сканер карты лица или радужки глаза')
    face_unlock = models.BooleanField(default=True, verbose_name='Разблокировка по лицу')
    registering_the_force_of_pressing = models.BooleanField(default=True, verbose_name='Регистрация силы нажатий')
    heart_rate_monitor = models.BooleanField(default=True, verbose_name='Монитор сердечного ритма')
    work_with_gloves = models.BooleanField(default=True, verbose_name='Работа в перчатках')
    ir_transmitter = models.BooleanField(default=True, verbose_name='ИК-передатчик')
    fm_receiver = models.BooleanField(default=True, verbose_name='FM-приемник')
    wireless_charging = models.BooleanField(default=True, verbose_name='Беспроводная зарядка')
    reverse_wireless_charging = models.BooleanField(default=True, verbose_name='Обратная беспроводная зарядка')
    fast_charging = models.BooleanField(default=True, verbose_name='Быстрая зарядка')
    accelerometer = models.BooleanField(default=True, verbose_name='Акселерометр')
    gyroscope = models.BooleanField(default=True, verbose_name='Гироскоп')
    light_sensor = models.BooleanField(default=True, verbose_name='Датчик освещенности')
    barometer = models.BooleanField(default=True, verbose_name='Барометр')
    ant = models.BooleanField(default=True, verbose_name='ANT+')
    gps = models.BooleanField(default=True, verbose_name='GPS')
    glonass = models.BooleanField(default=True, verbose_name='GLONASS')
    beidou = models.BooleanField(default=True, verbose_name='Beidou')
    edge = models.BooleanField(default=True, verbose_name='Передача данных EDGE')
    hspa = models.BooleanField(default=True, verbose_name='HSPA')
    hspa_plus = models.BooleanField(default=True, verbose_name='HSPA+')
    lte = models.BooleanField(default=True, verbose_name='LTE')
    five_g = models.BooleanField(default=True, verbose_name='5G')
    bluetooth = models.CharField(max_length=255, verbose_name='Bluetooth')
    audio_output = models.CharField(max_length=255, verbose_name='Аудиовыход')
    wifi = models.CharField(max_length=255, verbose_name='Wi-Fi')
    microusb_connector = models.CharField(max_length=255, verbose_name='Разъём подключения')
    hdmi = models.BooleanField(default=True, verbose_name='HDMI-выход')
    nfs = models.BooleanField(default=True, verbose_name='NFS')
    battery_type = models.CharField(max_length=255, verbose_name='Тип аккумулятора')
    battery_capacity = models.CharField(max_length=255, verbose_name='Ёмкость аккумулятора')
    non_removable = models.BooleanField(default=True, verbose_name='Несъёмный аккумулятор')
    contents_of_delivery = models.CharField(max_length=255, verbose_name='Комплект поставки')
    language = models.CharField(max_length=2, verbose_name='Выбор языка')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    class Meta:
        verbose_name = 'Смартфон'
        verbose_name_plural = 'Смартфоны'


class VideoCards(Product):
    """Видеокарты"""
    market_launch_date = models.CharField(max_length=255, verbose_name='Дата выхода на рынок')
    interface = models.CharField(max_length=255, verbose_name='Интерфейс')
    gpu_manufacturer = models.CharField(max_length=255, verbose_name='Производитель графического процессора')
    gpu = models.CharField(max_length=255, verbose_name='Графический процессор')
    overclocked_version = models.BooleanField(default=True, verbose_name='Разогнанная версия')
    lhr = models.BooleanField(default=True, verbose_name='Защита от майнинга (LHR)')
    base_gpu_frequency = models.CharField(max_length=255, verbose_name='Базовая частота графического процессора')
    max_gpu_frequency = models.CharField(max_length=255, verbose_name='Максимальная частота графического процессора')
    number_of_stream_processors = models.CharField(max_length=255, verbose_name='Количество потоковых процессоров')
    video_memory = models.CharField(max_length=255, verbose_name='Видеопамять')
    type_video_memory = models.CharField(max_length=255, verbose_name='Тип видеопамяти')
    effective_memory_frequency = models.CharField(max_length=255, verbose_name='Эффективная частота памяти')
    memory_bandwidth = models.CharField(max_length=255, verbose_name='Пропускная способность памяти')
    memory_bus_width = models.CharField(max_length=255, verbose_name='Ширина шины памяти')
    directx_support = models.CharField(max_length=255, verbose_name='Поддержка DirectX')
    sli_crossfire_support = models.BooleanField(default=True, verbose_name='Поддержка SLI/CrossFire')
    power_connectors = models.CharField(max_length=255, verbose_name='Разъемы питания')
    recommended_power_supply = models.CharField(max_length=255, verbose_name='Рекомендуемый блок питания')
    air_cooling = models.BooleanField(default=True, verbose_name='Охлаждение воздушное')
    water_cooling = models.BooleanField(default=True, verbose_name='Охлаждение жидкостное')
    cooling_system_thickness = models.CharField(max_length=255, verbose_name='Толщина системы охлаждения')
    card_length = models.CharField(max_length=255, verbose_name='Длина видеокарты')
    card_height = models.CharField(max_length=255, verbose_name='Высота видеокарты')
    vga = models.BooleanField(default=True, verbose_name='VGA')
    dvi = models.BooleanField(default=True, verbose_name='DVI')
    hdmi = models.BooleanField(default=True, verbose_name='HDMI')
    mini_hdmi = models.BooleanField(default=True, verbose_name='mini HDMI')
    display_port = models.BooleanField(default=True, verbose_name='DisplayPort')
    mini_display_port = models.BooleanField(default=True, verbose_name='mini DisplayPort')
    vesa_stereo = models.BooleanField(default=True, verbose_name='VESA Stereo')
    usb_type_c = models.BooleanField(default=True, verbose_name='USB Type-C')
    language = models.CharField(max_length=2, verbose_name='Выбор языка')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    class Meta:
        verbose_name = 'Видеокарта'
        verbose_name_plural = 'Видеокарты'


class Processors(Product):
    """Процессоры"""
    market_launch_date = models.CharField(max_length=255, verbose_name='Дата выхода на рынок')
    the_lineup = models.CharField(max_length=255, verbose_name='Модельный ряд')
    delivery_type = models.CharField(max_length=255, verbose_name='Тип поставки')
    cooling_included = models.BooleanField(default=True, verbose_name='Охлаждение в комплекте')
    crystal_code_name = models.CharField(max_length=255, verbose_name='Кодовое название кристалла')
    socket = models.CharField(max_length=255, verbose_name='Сокет')
    number_of_cores = models.CharField(max_length=255, verbose_name='Количество ядер')
    maximum_number_of_threads = models.CharField(max_length=255, verbose_name='Максимальное количество потоков')
    base_clock_frequency = models.CharField(max_length=255, verbose_name='Базовая тактовая частота')
    max_frequency = models.CharField(max_length=255, verbose_name='Максимальная частота')
    cash_l2 = models.CharField(max_length=255, verbose_name='Кэш L2')
    cash_l3 = models.CharField(max_length=255, verbose_name='Кэш L3')
    memory_support = models.CharField(max_length=255, verbose_name='Поддержка памяти')
    number_of_memory_channels = models.CharField(max_length=255, verbose_name='Количество каналов памяти')
    max_memory_frequency = models.CharField(max_length=255, verbose_name='Макс. частота памяти')
    gpu_express_controller = models.CharField(max_length=255, verbose_name='Встроенный контроллер PCI Express')
    integrated_graphics = models.BooleanField(default=True, verbose_name='Встроенная графика')
    tdp = models.CharField(max_length=255, verbose_name='Расчетная тепловая мощность (TDP)')
    technical_process = models.CharField(max_length=255, verbose_name='Техпроцесс')
    kernel_multi_threading = models.BooleanField(default=True, verbose_name='Многопоточность ядра')
    language = models.CharField(max_length=2, verbose_name='Выбор языка')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    class Meta:
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'


class Motherboard(Product):
    """Материнские платы"""
    market_launch_date = models.CharField(max_length=255, verbose_name='Дата выхода на рынок')
    processor_support = models.CharField(max_length=255, verbose_name='Поддержка процессоров')
    socket = models.CharField(max_length=255, verbose_name='Сокет')
    chipset = models.CharField(max_length=255, verbose_name='Чипсет')
    form_factor = models.CharField(max_length=255, verbose_name='Форм-фактор')
    backlight = models.BooleanField(default=True, verbose_name='Подсветка')
    memory_type = models.CharField(max_length=255, verbose_name='Тип памяти')
    number_of_memory_slots = models.CharField(max_length=255, verbose_name='Количество слотов памяти')
    max_memory = models.CharField(max_length=255, verbose_name='Максимальный объём памяти')
    memory_mode = models.CharField(max_length=255, verbose_name='Режим памяти')
    max_memory_frequency = models.CharField(max_length=255, verbose_name='Максимальная частота памяти')
    ver_pcl_express = models.CharField(max_length=255, verbose_name='Версия PCI Express')
    pcl_express_x16 = models.BooleanField(default=True, verbose_name='PCI Express x16')
    total_pcl_express_x16 = models.IntegerField(default=1, verbose_name='Количество PCI Express x16')
    pcl_express_2_x16 = models.BooleanField(default=True, verbose_name='PCI Express 2.0 x16')
    total_pcl_express_2_x16 = models.IntegerField(default=1, verbose_name='Количество PCI Express 2.0 x16')
    pcl_express_x1 = models.BooleanField(default=True, verbose_name='PCI Express x1')
    total_pcl_express_x1 = models.IntegerField(default=1, verbose_name='Количество PCI Express x1')
    pcl_express_2_x1 = models.BooleanField(default=True, verbose_name='Из них PCI Express 2.0 x1')
    total_pcl_express_2_x1 = models.IntegerField(default=1, verbose_name='Количество PCI Express 2.0 x1')
    pcl_express_x4 = models.BooleanField(default=True, verbose_name='Из них PCI Express x4')
    total_pcl_express_2_x4 = models.IntegerField(default=1, verbose_name='Количество PCI Express 2.0 x4')
    pcl_express_x8 = models.BooleanField(default=True, verbose_name='Из них PCI Express x8')
    total_pcl_express_2_x8 = models.IntegerField(default=1, verbose_name='Количество PCI Express 2.0 x8')
    pcl = models.BooleanField(default=True, verbose_name='PCI')
    m2 = models.BooleanField(default=True, verbose_name='Интерфейс ssd M.2')
    total_m2 = models.CharField(max_length=255, verbose_name='Количество ssd M.2')
    sata_3 = models.BooleanField(default=True, verbose_name='Интерфейс SATA 3.0')
    total_sata_3 = models.CharField(max_length=255, verbose_name='Количество SATA 3.0')
    raid = models.CharField(max_length=255, verbose_name='RAID')
    slot_wifi = models.BooleanField(default=True, verbose_name='Слот для модуля Wi-Fi')
    wifi = models.BooleanField(default=True, verbose_name='Wi-Fi')
    bluetooth = models.BooleanField(default=True, verbose_name='Bluetooth')
    ethernet = models.BooleanField(default=True, verbose_name='Ethernet')
    integrated_graphics_support = models.BooleanField(default=True, verbose_name='Поддержка встроенной графики')
    sli_crossfire_support = models.BooleanField(default=True, verbose_name='Поддержка SLi/CrossFire')
    built_in_sound = models.CharField(max_length=255, verbose_name='Встроенный звук')
    sound_scheme = models.CharField(max_length=255, verbose_name='Звуковая схема')
    usb_2 = models.BooleanField(default=True, verbose_name='USB 2.0')
    total_usb_2 = models.IntegerField(default=1, verbose_name='Количество USB 2.0')
    usb_3_gen1_type_a_5gbit = models.BooleanField(default=True, verbose_name='USB 3.2 Gen1 Type-A (5 Гбит/с)')
    total_usb_3_gen1_type_a_5gbit = models.IntegerField(default=1, verbose_name='Всего USB 3.2 Gen1 Type-A (5 Гбит/с)')
    usb_3_gen2_type_a_10gbit = models.BooleanField(default=True, verbose_name='USB 3.2 Gen2 Type-A (10 Гбит/с)')
    total_usb_3_gen2_type_a_10gbit = models.IntegerField(default=1,
                                                         verbose_name='Всего USB 3.2 Gen2 Type-A (10 Гбит/с)')
    usb_3_gen1_type_c_5gbit = models.BooleanField(default=True, verbose_name='USB 3.2 Gen1 Type-C (5 Гбит/с)')
    total_usb_3_gen1_type_c_5gbit = models.IntegerField(default=1, verbose_name='Всего USB 3.2 Gen1 Type-C (5 Гбит/с)')
    usb_3_gen2_type_c_10gbit = models.BooleanField(default=True, verbose_name='USB 3.2 Gen2 Type-C (10 Гбит/с)')
    total_usb_3_gen2_type_c_10gbit = models.IntegerField(default=1,
                                                         verbose_name='Всего USB 3.2 Gen2 Type-C (10 Гбит/с)')
    usb_c_thunderbolt3 = models.BooleanField(default=True, verbose_name='USB-C (Thunderbolt 3)')
    s_pdif_digital_output = models.BooleanField(default=True, verbose_name='Цифровой выход S/PDIF')
    audio_jack = models.BooleanField(default=True, verbose_name='Аудио (3.5 мм jack)')
    total_audio_jack = models.IntegerField(default=1, verbose_name='Всего аудио (3.5 мм jack)')
    com = models.BooleanField(default=True, verbose_name='COM')
    lpt = models.BooleanField(default=True, verbose_name='LPT')
    ps_2 = models.BooleanField(default=True, verbose_name='PS/2')
    total_ps_2 = models.IntegerField(default=1, verbose_name='Всего PS/2')
    display_port = models.BooleanField(default=True, verbose_name='DisplayPort')
    mini_display_port = models.BooleanField(default=True, verbose_name='mini DisplayPort ')
    vga = models.BooleanField(default=True, verbose_name='VGA (D-Sub)')
    dvi = models.BooleanField(default=True, verbose_name='DVI')
    hdmi = models.BooleanField(default=True, verbose_name='HDMI')
    total_hdmi = models.IntegerField(default=1, verbose_name='Всего HDMI')
    cpu_fan_connectors = models.BooleanField(default=True, verbose_name='Разъемы для вентилятора ЦП')
    total_cpu_fan_connectors = models.CharField(max_length=255, verbose_name='Всего разъемов для вентилятора ЦП')
    sockets_for_cbo_processor = models.BooleanField(default=True, verbose_name='Разъемы для СВО процессора')
    total_sockets_for_cbo_processor = models.CharField(max_length=255,
                                                       verbose_name='Всего разъемов для СВО процессора')
    case_fan_connectors = models.BooleanField(default=True, verbose_name='Разъемы для корпусных вентиляторов')
    total_case_fan_connectors = models.IntegerField(default=1, verbose_name='Всего разъемов для корпусных вентиляторов')
    enable_5v_argb_lighting_connectors = models.BooleanField(default=True,
                                                             verbose_name='Разъемы для подсветки ARGB 5В')
    total_5v_argb_lighting_connectors = models.IntegerField(default=1,
                                                            verbose_name='Всего разъемов для подсветки ARGB 5В')
    enable_12v_lighting_connectors = models.BooleanField(default=True, verbose_name='Разъемы для подсветки RGB 12В')
    total_12v_lighting_connectors = models.IntegerField(default=1, verbose_name='Всего разъемов для подсветки RGB 12В')
    length = models.CharField(max_length=255, verbose_name='Длина')
    width = models.CharField(max_length=255, verbose_name='Ширина')
    language = models.CharField(max_length=2, verbose_name='Выбор языка')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    class Meta:
        verbose_name = 'Материнская плата'
        verbose_name_plural = 'Материнские платы'


class RAM(Product):
    """Оперативная память"""
    kit = models.CharField(max_length=255, verbose_name='Набор')
    capacity = models.CharField(max_length=255, verbose_name='Объем')
    type = models.CharField(max_length=255, verbose_name='Тип памяти')
    ecc = models.BooleanField(default=True, verbose_name='ECC')
    frequency = models.CharField(max_length=255, verbose_name='Частота')
    pc_index = models.CharField(max_length=255, verbose_name='PC-индекс')
    cas_latency = models.CharField(max_length=255, verbose_name='CAS Latency')
    timings = models.CharField(max_length=255, verbose_name='Тайминги')
    supply_voltage = models.CharField(max_length=255, verbose_name='Напряжение питания')
    xmp_profile = models.BooleanField(default=True, verbose_name='Профили XMP')
    amp_profile = models.BooleanField(default=True, verbose_name='Профили AMP')
    cooling = models.BooleanField(default=True, verbose_name='Охлаждение')
    low_module = models.BooleanField(default=True, verbose_name='Низкопрофильный модуль')
    illumination = models.BooleanField(default=True, verbose_name='Подсветка элементов платы')
    color = models.CharField(max_length=255, verbose_name='Цвет')
    language = models.CharField(max_length=2, verbose_name='Выбор языка')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    class Meta:
        verbose_name = 'Оперативная память'
        verbose_name_plural = 'Оперативные памяти'


class Coolers(Product):
    """Системы охлаждения"""
    type = models.CharField(max_length=255, verbose_name='Тип')
    cooling_type = models.CharField(max_length=255, verbose_name='Тип охлаждения')
    color = models.CharField(max_length=255, verbose_name='Цвет')
    socket = models.CharField(max_length=255, verbose_name='Сокет')
    power_dissipation = models.CharField(max_length=255, verbose_name='Рассеиваемая мощность')
    radiator_metal = models.CharField(max_length=255, verbose_name='Материал радиатора')
    heat_pipes = models.BooleanField(default=True, verbose_name='Тепловые трубки')
    total_heat_pipes = models.IntegerField(default=1, verbose_name='Всего тепловых трубок')
    evaporation = models.BooleanField(default=True, verbose_name='Испарительные камеры')
    fan_diameter = models.CharField(max_length=255, verbose_name='Диаметр вентилятора')
    total_fans = models.IntegerField(default=1, verbose_name='Количество вентиляторов')
    bearing = models.CharField(max_length=255, verbose_name='Подшипник')
    max_rotation_speed = models.CharField(max_length=255, verbose_name='Максимальная скорость вращения')
    rotation_speed_control = models.BooleanField(default=True, verbose_name='Контроль скорости вращения (PWM)')
    thermal_control = models.BooleanField(default=True, verbose_name='Термоконтроль')
    connection_type = models.CharField(max_length=255, verbose_name='Тип подключения')
    led = models.BooleanField(default=True, verbose_name='LED-подсветка')
    vibration_isolation = models.BooleanField(default=True, verbose_name='Виброизоляция')
    noise_lvl = models.CharField(max_length=255, verbose_name='Уровень шума')
    width = models.CharField(max_length=255, verbose_name='Ширина')
    depth = models.CharField(max_length=255, verbose_name='Глубина')
    height = models.CharField(max_length=255, verbose_name='Высота')
    weight = models.CharField(max_length=255, verbose_name='Вес')
    language = models.CharField(max_length=2, verbose_name='Выбор языка')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    class Meta:
        verbose_name = 'Система охлаждения'
        verbose_name_plural = 'Системы охлаждения'


class SSD(Product):
    """SSD"""
    market_launch_date = models.CharField(max_length=255, verbose_name='Дата выхода на рынок')
    capacity = models.CharField(max_length=255, verbose_name='Объём')
    form_factor = models.CharField(max_length=255, verbose_name='Форм-фактор')
    interface = models.CharField(max_length=255, verbose_name='Интерфейс')
    chip_type_flash = models.CharField(max_length=255, verbose_name='Тип микросхем Flash')
    controller = models.CharField(max_length=255, verbose_name='Контроллер')
    m2_device_dimensions = models.CharField(max_length=255, verbose_name='Размеры устройств M.2')
    recording_resource = models.CharField(max_length=255, verbose_name='Ресурс записи')
    buffer = models.CharField(max_length=255, verbose_name='Буфер')
    hardware_encryption = models.BooleanField(default=True, verbose_name='Аппаратное шифрование')
    sequential_read_speed = models.CharField(max_length=255, verbose_name='Скорость последовательного чтения')
    sequential_write_speed = models.CharField(max_length=255, verbose_name='Скорость последовательной записи')
    average_random_read_speed = models.CharField(max_length=255, verbose_name='Средняя скорость случайного чтения')
    average_random_write_speed = models.CharField(max_length=255, verbose_name='Средняя скорость случайной записи')
    power_consumption_1 = models.CharField(max_length=255, verbose_name='Энергопотребление (чтение/запись)')
    power_consumption_2 = models.CharField(max_length=255, verbose_name='Энергопотребление (ожидание)')
    time_between_failures = models.CharField(max_length=255, verbose_name='Время наработки на отказ (МТBF)')
    cooling = models.BooleanField(default=True, verbose_name='Охлаждение')
    thickness = models.CharField(max_length=255, verbose_name='Толщина')
    adapter = models.BooleanField(default=True, verbose_name='Адаптер 3.5')
    language = models.CharField(max_length=2, verbose_name='Выбор языка')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    class Meta:
        verbose_name = 'SSD'
        verbose_name_plural = 'SSD'


class HDD(Product):
    """HDD"""
    drive_type = models.CharField(max_length=255, verbose_name='Тип накопителя')
    capacity = models.CharField(max_length=255, verbose_name='Объём')
    form_factor = models.CharField(max_length=255, verbose_name='Форм-фактор')
    interface = models.CharField(max_length=255, verbose_name='Интерфейс')
    spindle_speed = models.CharField(max_length=255, verbose_name='Скорость вращения шпинделя')
    buffer = models.CharField(max_length=255, verbose_name='Буфер')
    read_write_noise = models.CharField(max_length=255, verbose_name='Уровень шума при чтении/записи')
    standby_noise = models.CharField(max_length=255, verbose_name='Уровень шума в режиме ожидания')
    shock_during_operation = models.CharField(max_length=255, verbose_name='Ударная нагрузка при работе')
    non_operation_shock = models.CharField(max_length=255, verbose_name='Ударная нагрузка в нерабочем состоянии')
    power_consumption_1 = models.CharField(max_length=255, verbose_name='Энергопотребление (чтение/запись)')
    power_consumption_2 = models.CharField(max_length=255, verbose_name='Энергопотребление (ожидание)')
    thickness = models.CharField(max_length=255, verbose_name='Толщина')
    language = models.CharField(max_length=2, verbose_name='Выбор языка')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    class Meta:
        verbose_name = 'HDD'
        verbose_name_plural = 'HDD'


class Case(Product):
    """Корпуса"""
    power_supply = models.CharField(max_length=255, verbose_name='Блок питания')
    type_of_case = models.CharField(max_length=255, verbose_name='Тип корпуса')
    game_case = models.BooleanField(default=True, verbose_name='Игровой корпус')
    case_color = models.CharField(max_length=255, verbose_name='Цвет корпуса')
    case_material = models.CharField(max_length=255, verbose_name='Материал корпуса')
    transparent_window = models.BooleanField(default=True, verbose_name='Прозрачное окно')
    max_motherboard_size = models.CharField(max_length=255, verbose_name='Макс.размер материнской платы')
    compatible_motherboard = models.CharField(max_length=255, verbose_name='Совместимые материнские платы')
    power_supply_loc = models.CharField(max_length=255, verbose_name='Расположение блока питания')
    fans_included = models.BooleanField(default=True, verbose_name='Вентиляторы в комплекте')
    liquid_cooling_support = models.BooleanField(default=True, verbose_name='Поддержка жидкостного охлаждения')
    number_of_places_for_fans = models.IntegerField(default=1, verbose_name='Количество мест для вентиляторов')
    installed_coolers = models.IntegerField(default=1, verbose_name='Установленные кулеры')
    noise_isolation = models.BooleanField(default=True, verbose_name='Шумоизоляция')
    bays_5_inches = models.BooleanField(default=True, verbose_name='Отсеки 5.25 дюймов')
    external_bays_inches = models.BooleanField(default=True, verbose_name='Внешние отсеки 3.5 дюймов')
    internal_bays_inches = models.BooleanField(default=True, verbose_name='Внутренние отсеки 3.5 дюймов')
    bays_2_inches = models.BooleanField(default=True, verbose_name='Отсеки 2.5 дюймов')
    remove_hard_drive_cage = models.BooleanField(default=True, verbose_name='Съёмная корзина жестких дисков')
    screwless_drive_mounting = models.BooleanField(default=True, verbose_name='Безвинтовое крепление дисков')
    expansion_slots = models.IntegerField(default=1, verbose_name='Слоты расширения')
    dust_filters = models.BooleanField(default=True, verbose_name='Пылевые фильтры')
    backlight_housing = models.BooleanField(default=True, verbose_name='Подсветка корпуса')
    backlight_controller = models.BooleanField(default=True, verbose_name='Контроллер подсветки')
    fan_rotation_controller = models.BooleanField(default=True, verbose_name='Контроллер вращения вентиляторов')
    max_video_card_length = models.CharField(max_length=255, verbose_name='Макс.длина видеокарты')
    max_cpu_cooler_height = models.CharField(max_length=255, verbose_name='Макс.высота процессорного кулера')
    max_power_supply_length = models.CharField(max_length=255, verbose_name='Макс. длина блока питания')
    vesa = models.BooleanField(default=True, verbose_name='Крепление VESA')
    door = models.BooleanField(default=True, verbose_name='Дверца')
    lock = models.BooleanField(default=True, verbose_name='Замок')
    info_display = models.BooleanField(default=True, verbose_name='Информационный дисплей')
    usb_2 = models.BooleanField(default=True, verbose_name='USB 2.0')
    usb_3_gen1_type_a_5gbit = models.BooleanField(default=True, verbose_name='USB 3.2 Gen1 Type-A (5 Гбит/с)')
    usb_3_gen1_type_c_5gbit = models.BooleanField(default=True, verbose_name='USB 3.2 Gen1 Type-C (5 Гбит/с)')
    firewire = models.BooleanField(default=True, verbose_name='FireWire (IEEE 1394, iLink)')
    esata = models.BooleanField(default=True, verbose_name='eSATA')
    hard_drive_docking_station = models.BooleanField(default=True, verbose_name='Док-станция для винчестеров')
    cardreader = models.BooleanField(default=True, verbose_name='Кардридер')
    audio_output = models.BooleanField(default=True, verbose_name='Аудио выход')
    micro_output = models.BooleanField(default=True, verbose_name='Вход для микрофона')
    height = models.CharField(max_length=255, verbose_name='Высота')
    width = models.CharField(max_length=255, verbose_name='Ширина')
    depth = models.CharField(max_length=255, verbose_name='Глубина')
    weight = models.CharField(max_length=255, verbose_name='Вес')
    language = models.CharField(max_length=2, verbose_name='Выбор языка')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпуса'


class PowerSupply(Product):
    """Блоки питания"""
    appointment = models.CharField(max_length=255, verbose_name='Назначение')
    power = models.CharField(max_length=255, verbose_name='Мощность')
    power_supply_standard = models.CharField(max_length=255, verbose_name='Стандарт блока питания')
    mains_input_voltage_range = models.CharField(max_length=255, verbose_name='Диапазон входного напряжения сети')
    number_of_separate_lines_12v = models.IntegerField(default=1, verbose_name='Количество отдельных линий +12V')
    max_line_current_12v = models.CharField(max_length=255, verbose_name='Макс. ток по линии +12V')
    combined_load_12v = models.CharField(max_length=255, verbose_name='Комбинированная нагрузка по +12V')
    power_factor_correction = models.BooleanField(default=True, verbose_name='Коррекция фактора мощности (PFC)')
    efficiency = models.CharField(max_length=255, verbose_name='КПД')
    certificate_80_plus = models.BooleanField(default=True, verbose_name='Сертификат 80 PLUS')
    power_supply_fan_size = models.CharField(max_length=255, verbose_name='Размер вентилятора блока питания')
    total_fans = models.IntegerField(default=1, verbose_name='Количество вентиляторов')
    fan_illumination = models.BooleanField(default=True, verbose_name='Подсветка вентилятора')
    case_illumination = models.BooleanField(default=True, verbose_name='Подсветка корпуса')
    power_cable_length = models.CharField(max_length=255, verbose_name='Длина кабеля питания')
    modular_power_cable_connection = models.BooleanField(default=True,
                                                         verbose_name='Модульное подключение кабелей питания')
    motherboard_power = models.CharField(max_length=255, verbose_name='Питание материнской платы')
    cpu_4_pin = models.BooleanField(default=True, verbose_name='CPU 4 pin')
    cpu_8_pin = models.BooleanField(default=True, verbose_name='CPU 8 pin')
    fdd_4_pin = models.BooleanField(default=True, verbose_name='FDD 4 pin')
    ide_4_pin = models.BooleanField(default=True, verbose_name='IDE 4 pin')
    sata = models.BooleanField(default=True, verbose_name='SATA')
    pcle_6_pin = models.BooleanField(default=True, verbose_name='PCIe 6 pin')
    pcle_8_pin = models.BooleanField(default=True, verbose_name='PCIe 8 pin')
    usb_power = models.BooleanField(default=True, verbose_name='USB Power')
    height = models.CharField(max_length=255, verbose_name='Высота')
    width = models.CharField(max_length=255, verbose_name='Ширина')
    depth = models.CharField(max_length=255, verbose_name='Глубина')
    weight = models.CharField(max_length=255, verbose_name='Вес')
    language = models.CharField(max_length=2, verbose_name='Выбор языка')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    class Meta:
        verbose_name = 'Блок питания'
        verbose_name_plural = 'Блоки питания'


class CartProduct(models.Model):
    """Товар в корзине"""
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена')

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.content_object.title)

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'


class Cart(models.Model):
    """Корзина"""
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Customer(models.Model):
    """Информация об покупателе"""
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class TabIcons(models.Model):
    """Техническая таблица"""
    info = models.CharField(max_length=20, verbose_name='Описание')
    icon_image = models.ImageField(verbose_name='Иконки svg-формат', upload_to='web_media/tab_icons')

    def __str__(self):
        return self.info

    class Meta:
        verbose_name = 'Дополнительная информация'
        verbose_name_plural = 'Дополнительная информация'


class Post(models.Model):
    """Последние обновления"""
    main_title = models.CharField(max_length=255, verbose_name='Тема')
    title = models.CharField(max_length=1024, verbose_name='Описание')
    slug = models.SlugField()

    def __str__(self):
        return self.main_title

    class Meta:
        verbose_name = 'Последнее обновление'
        verbose_name_plural = 'Последние обновления'
