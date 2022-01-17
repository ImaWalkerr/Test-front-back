from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'main_title',
                    'title')
    list_display_links = ('main_title',)


class NotebookAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if not instance.usb_2:
            self.fields['total_usb_2'].widget.attrs.update({
                'readonly': True, 'style': 'background: lightgray;'
            })

    def clean(self):
        if not self.cleaned_data['usb_2']:
            self.cleaned_data['total_usb_2'] = None
        return self.cleaned_data


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'slug')

    list_display_links = ('name',)


@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = NotebookAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(queryset=Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('date',
                    'product_line',
                    'platform_codename',
                    'language')

    list_display_links = ('product_line',)

    list_filter = ('date',
                   'product_line',
                   'platform_codename',
                   'language')

    fieldsets = (
        ('Абстрактная модель - Товары (общие данные)', {
            'fields': [
                ('category',
                 'slug'),
                ('title',
                 'company'),
                ('image',
                 'description',
                 'price')
            ]
        }),
        ('Общая информация', {
            'fields': [
                ('date',
                 'product_line',
                 'type')
            ]
        }),
        ('Процессор', {
            'fields': [
                ('platform_codename',
                 'processor_model',
                 'number_of_cores_cpu',
                 'number_of_threads_cpu'),
                ('clock_frequency_cpu',
                 'turbo_frequency_cpu',
                 'cpu_power_consumption'),
                'cpu_graphics'
            ]
        }),
        ('Конструкция', {
            'fields': [
                ('case_material',
                 'case_color',
                 'case_backlight'),
                'protected_case',
                ('cover_material',
                 'cover_color')
            ]
        }),
        ('Размеры и вес', {
            'fields': [
                ('length',
                 'width',
                 'thickness',
                 'height')
            ]
        }),
        ('Экран', {
            'fields': [
                ('screen_diagonal',
                 'screen_resolution',
                 'matrix_frequency',
                 'screen_technology'),
                ('screen_surface',
                 'screen_support',
                 'screen_protection',
                 'screen_info')
            ]
        }),
        ('Оперативная память', {
            'fields': [
                'ram_type',
                'ram_frequency',
                'ram_memory',
                'max_ram_memory',
                'memory_slots',
                'free_memory_slots'
            ]
        }),
        ('Хранение данных', {
            'fields': [
                ('configuration_drive_type',
                 'drive_type',
                 'drive_capacity'),
                ('number_of_ssd_slots',
                 'interface_ssd',
                 'optical_drive_unit'),
                'memory_cards'
            ]
        }),
        ('Графика', {
            'fields': [
                ('discrete_graphics',
                 'graphics_card_model',
                 'local_video_memory'),
                ('graphics_card_feature',
                 'additional_graphics_card_feature')
            ]
        }),
        ('Камера и звук', {
            'fields': [
                'camera',
                'built_in_microphone',
                'built_in_speakers'
            ]
        }),
        ('Клавиатура и тачпад', {
            'fields': [
                'numpad',
                'backlit_keyboard',
                'factory_cyrillic_on_keys',
                'cursor_control',
                'multimedia_touchpad'
            ]
        }),
        ('Функции', {
            'fields': [
                'privacy_protection_features'
            ]
        }),
        ('Интерфейсы', {
            'fields': [
                ('nfs',
                 'bluetooth',
                 'lan',
                 'wifi',
                 'mobile'),
                ('usb_2',
                 'total_usb_2',
                 'total_usb_type_a',
                 'usb_3_2_gen1_type_a_5gbit',
                 'total_usb_3_2_gen1_type_a_5gbit',
                 'usb_3_2_gen1_type_a_10gbit',
                 'total_usb_type_c',
                 'usb_3_2_gen1_type_c_5gbit',
                 'total_usb_3_2_gen1_type_c_5gbit',
                 'usb_3_2_gen2_type_c_10gbit',
                 'total_usb_3_2_gen2_type_c_10gbit',
                 'usb_3_2_gen2x2_20gbit',
                 'total_usb_3_2_gen2x2_20gbit',
                 'usb_4'),
                ('max_usb_speed',
                 'alternative_modes_usb_type_c',
                 'vga',
                 'hdmi',
                 'mini_display_port',
                 'audio_outputs')
            ]
        }),
        ('Аккумулятор и время работы', {
            'fields': [
                'battery_cells',
                'energy_reserve',
                'charge_via_usb_type_c',
                'usb_c_power_adapter'
            ]
        }),
        ('Комплектация', {
            'fields': [
                'operation_system',
                'additional_equipment'
            ]
        }),
    )


@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(queryset=Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('date',
                    'mobile_operation_system',
                    'platform',
                    'language')

    list_display_links = ('platform',)

    list_filter = ('date',
                   'mobile_operation_system',
                   'platform',
                   'language')

    fieldsets = (
        ('Абстрактная модель - Товары (общие данные)', {
            'fields': [
                ('category',
                 'slug'),
                ('title',
                 'company'),
                ('image',
                 'description',
                 'price')
            ]
        }),
        ('Основные', {
            'fields': [
                ('date',
                 'mobile_operation_system',
                 'ver_mobile_operation_system'),
                ('screen_size',
                 'screen_resolution_mobile'),
                ('ram_mobile',
                 'flash_memory',
                 'memory_card_support'),
                ('built_in_camera',
                 'num_of_main_cam',
                 'num_of_matrix_points',
                 'max_video_resolution'),
                ('num_of_sim_cards',
                 'sim_card_format')
            ]
        }),
        ('Процессор', {
            'fields': [
                ('platform',
                 'cpu',
                 'cpu_clock_speed',
                 'num_of_cores'),
                ('microarchitecture_cpu',
                 'cpu_size',
                 'technical_process'),
                ('graphics_accelerator',
                 'gpu_frequency')
            ]
        }),
        ('Конструкция', {
            'fields': [
                ('body_design',
                 'replaceable_panels',
                 'body_material'),
                ('back_cover_material',
                 'body_color',
                 'front_panel_color'),
                ('shockproof_housing',
                 'protection',
                 'physical_qwerty_keyboard'),
                ('front_camera_location',
                 'fingerprint_scanner_location',
                 'button_sos'),
            ]
        }),
        ('Размеры и вес', {
            'fields': [
                'length',
                'width',
                'thickness',
                'height'
            ]
        }),
        ('Экран', {
            'fields': [
                ('screen_technology',
                 'num_of_screen_colors',
                 'screen_res',
                 'aspect_ratio'),
                ('refresh_rate',
                 'touch_screen',
                 'scratch_protection',
                 'sec_screen_technology')
            ]
        }),
        ('Основная камера', {
            'fields': [
                ('camera_specifications',
                 'additional_camera_modules',
                 'built_in_flash_main_camera',
                 'auto_focus_main_camera'),
                ('optical_stabilization_main_camera',
                 'diaphragm_main_camera',
                 'max_frames_per_second_main_camera')
            ]
        }),
        ('Фронтальная камера', {
            'fields': [
                ('front_camera',
                 'dual_camera',
                 'auto_focus_front_camera',
                 'optical_stabilization_front_camera'),
                ('built_in_flash_front_camera',
                 'max_frames_per_second',
                 'diaphragm_front_camera',
                 'max_frames_per_second_front_camera')
            ]
        }),
        ('Функции', {
            'fields': [
                ('stereo_speakers',
                 'fingerprint_scanner',
                 'face_or_iris_map_scanner',
                 'face_unlock'),
                ('registering_the_force_of_pressing',
                 'heart_rate_monitor',
                 'work_with_gloves',
                 'ir_transmitter'),
                ('fm_receiver',
                 'wireless_charging',
                 'reverse_wireless_charging',
                 'fast_charging'),
            ]
        }),
        ('Датчики', {
            'fields': [
                ('accelerometer',
                 'gyroscope',
                 'light_sensor',
                 'barometer',
                 'ant')
            ]
        }),
        ('Навигация', {
            'fields': [
                ('gps',
                 'glonass',
                 'beidou')
            ]
        }),
        ('Передача данных', {
            'fields': [
                ('edge',
                 'hspa',
                 'hspa_plus',
                 'lte',
                 'five_g')
            ]
        }),
        ('Интерфейсы', {
            'fields': [
                ('bluetooth',
                 'audio_output',
                 'wifi'),
                ('microusb_connector',
                 'hdmi',
                 'nfs')
            ]
        }),
        ('Аккумулятор и время работы', {
            'fields': [
                ('battery_type',
                 'battery_capacity',
                 'non_removable')
            ]
        }),
        ('Комплектация', {
            'fields': ['contents_of_delivery']
        }),
    )


@admin.register(VideoCards)
class VideoCardsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(queryset=Category.objects.filter(slug='videocards'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('interface',
                    'gpu_manufacturer',
                    'gpu',
                    'language')

    list_display_links = ('gpu',)

    list_filter = ('interface',
                   'gpu_manufacturer',
                   'gpu',
                   'language')

    fieldsets = (
        ('Абстрактная модель - Товары (общие данные)', {
            'fields': [
                ('category',
                 'slug'),
                ('title',
                 'company'),
                ('image',
                 'description',
                 'price')
            ]
        }),
        ('Основные', {
            'fields': [
                ('market_launch_date',
                 'interface',
                 'gpu_manufacturer'),
                ('gpu',
                 'overclocked_version',
                 'lhr')
            ]
        }),
        ('Технические характеристики', {
            'fields': [
                ('base_gpu_frequency',
                 'max_gpu_frequency',
                 'number_of_stream_processors',
                 'video_memory'),
                ('type_video_memory',
                 'effective_memory_frequency',
                 'memory_bandwidth',
                 'memory_bus_width'),
                ('directx_support',
                 'sli_crossfire_support',
                 'power_connectors',
                 'recommended_power_supply'),
                ('air_cooling',
                 'water_cooling',
                 'cooling_system_thickness',
                 'card_length',
                 'card_height')
            ]
        }),
        ('Интерфейсы', {
            'fields': [
                ('vga',
                 'dvi',
                 'hdmi'),
                ('mini_hdmi',
                 'display_port',
                 'mini_display_port'),
                ('vesa_stereo',
                 'usb_type_c')
            ]
        }),
    )


@admin.register(Processors)
class ProcessorsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(queryset=Category.objects.filter(slug='processors'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('the_lineup',
                    'delivery_type',
                    'crystal_code_name',
                    'language')

    list_display_links = ('the_lineup',)

    list_filter = ('the_lineup',
                   'delivery_type',
                   'crystal_code_name',
                   'language')

    fieldsets = (
        ('Абстрактная модель - Товары (общие данные)', {
            'fields': [
                ('category',
                 'slug'),
                ('title',
                 'company'),
                ('image',
                 'description',
                 'price')
            ]
        }),
        ('Общая информация', {
            'fields': ['market_launch_date']
        }),
        ('Технические характеристики', {
            'fields': [
                ('the_lineup',
                 'delivery_type',
                 'cooling_included',
                 'crystal_code_name',
                 'socket'),
                ('number_of_cores',
                 'maximum_number_of_threads',
                 'base_clock_frequency',
                 'max_frequency'),
                ('cash_l2',
                 'cash_l3',
                 'memory_support',
                 'max_memory_frequency'),
                ('gpu_express_controller',
                 'integrated_graphics',
                 'tdp',
                 'technical_process',
                 'kernel_multi_threading')
            ]
        }),
    )


@admin.register(Motherboard)
class MotherboardAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(queryset=Category.objects.filter(slug='motherboards'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('socket',
                    'chipset',
                    'form_factor',
                    'language')

    list_display_links = ('chipset',)

    list_filter = ('socket',
                   'chipset',
                   'form_factor',
                   'language')

    fieldsets = (
        ('Абстрактная модель - Товары (общие данные)', {
            'fields': [
                ('category',
                 'slug'),
                ('title',
                 'company'),
                ('image',
                 'description',
                 'price')
            ]
        }),
        ('Общая информация', {
            'fields': ['market_launch_date']
        }),
        ('Технические характеристики', {
            'fields': [
                ('processor_support',
                 'socket',
                 'chipset',
                 'form_factor'),
                'backlight'
            ]
        }),
        ('Память', {
            'fields': [
                'memory_type',
                'number_of_memory_slots',
                'max_memory',
                'memory_mode',
                'max_memory_frequency'
            ]
        }),
        ('Слоты расширения', {
            'fields': [
                ('ver_pcl_express',
                 'pcl_express_x16',
                 'total_pcl_express_x16'),
                ('pcl_express_2_x16',
                 'total_pcl_express_2_x16'),
                ('pcl_express_x1',
                 'total_pcl_express_x1'),
                ('pcl_express_2_x1',
                 'total_pcl_express_2_x1'),
                ('pcl_express_x4',
                 'total_pcl_express_2_x4'),
                ('pcl_express_x8',
                 'total_pcl_express_2_x8'),
                'pcl'
            ]
        }),
        ('Интерфейсы накопителей', {
            'fields': [
                ('m2',
                 'total_m2',
                 'sata_3',
                 'total_sata_3',
                 'raid')
            ]
        }),
        ('Сеть и связь', {
            'fields': [
                ('slot_wifi',
                 'wifi',
                 'bluetooth',
                 'ethernet')
            ]
        }),
        ('Аудио и Видео', {
            'fields': [
                ('integrated_graphics_support',
                 'sli_crossfire_support'),
                ('built_in_sound',
                 'sound_scheme')
            ]
        }),
        ('Разъемы на задней панели', {
            'fields': [
                ('usb_2',
                 'total_usb_2'),
                ('usb_3_gen1_type_a_5gbit',
                 'total_usb_3_gen1_type_a_5gbit'),
                ('usb_3_gen2_type_a_10gbit',
                 'total_usb_3_gen2_type_a_10gbit'),
                ('usb_3_gen1_type_c_5gbit',
                 'total_usb_3_gen1_type_c_5gbit'),
                ('usb_3_gen2_type_c_10gbit',
                 'total_usb_3_gen2_type_c_10gbit'),
                'usb_c_thunderbolt3',
                ('s_pdif_digital_output',
                 'audio_jack',
                 'total_audio_jack'),
                ('com',
                 'lpt',
                 'ps_2',
                 'total_ps_2'),
                ('display_port',
                 'mini_display_port',
                 'vga',
                 'dvi',
                 'hdmi',
                 'total_hdmi')
            ]
        }),
        ('Аудио и Видео', {
            'fields': [
                ('cpu_fan_connectors',
                 'total_cpu_fan_connectors'),
                ('sockets_for_cbo_processor',
                 'total_sockets_for_cbo_processor'),
                ('case_fan_connectors',
                 'total_case_fan_connectors'),
                ('enable_5v_argb_lighting_connectors',
                 'total_5v_argb_lighting_connectors'),
                ('enable_12v_lighting_connectors',
                 'total_12v_lighting_connectors')
            ]
        }),
        ('Габариты', {
            'fields': [
                'length',
                'width'
            ]
        }),
    )


@admin.register(RAM)
class RAMAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(queryset=Category.objects.filter(slug='ram'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('kit',
                    'capacity',
                    'type',
                    'language')

    list_display_links = ('kit',)

    list_filter = ('kit',
                   'capacity',
                   'type',
                   'language')

    fieldsets = (
        ('Абстрактная модель - Товары (общие данные)', {
            'fields': [
                ('category',
                 'slug'),
                ('title',
                 'company'),
                ('image',
                 'description',
                 'price')
            ]
        }),
        ('Основные', {
            'fields': [
                ('kit',
                 'capacity',
                 'type',
                 'ecc',
                 'frequency'),
                ('pc_index',
                 'cas_latency',
                 'timings',
                 'supply_voltage')
            ]
        }),
        ('Технические характеристики', {
            'fields': [
                'xmp_profile',
                'amp_profile'
            ]
        }),
        ('Конструкция', {
            'fields': [
                ('cooling',
                 'low_module'),
                ('illumination',
                 'color')
            ]
        }),
    )


@admin.register(Coolers)
class CoolersAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(queryset=Category.objects.filter(slug='coolers'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('type',
                    'cooling_type',
                    'language')

    list_display_links = ('type',)

    list_filter = ('type',
                   'cooling_type',
                   'language')

    fieldsets = (
        ('Абстрактная модель - Товары (общие данные)', {
            'fields': [
                ('category',
                 'slug'),
                ('title',
                 'company'),
                ('image',
                 'description',
                 'price')
            ]
        }),
        ('Основные', {
            'fields': [
                'type',
                'cooling_type',
                'color'
            ]
        }),
        ('Технические характеристики', {
            'fields': [
                'socket',
                ('power_dissipation',
                 'radiator_metal'),
                ('heat_pipes',
                 'total_heat_pipes',
                 'evaporation')
            ]
        }),
        ('Вентилятор', {
            'fields': [
                ('fan_diameter',
                 'total_fans'),
                ('bearing',
                 'max_rotation_speed'),
                ('rotation_speed_control',
                 'thermal_control'),
                ('connection_type',
                 'led'),
                ('vibration_isolation',
                 'noise_lvl'),
            ]
        }),
        ('Размеры и вес', {
            'fields': [
                ('width',
                 'depth'),
                ('height',
                 'weight')
            ]
        }),
    )


@admin.register(SSD)
class SSDAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(queryset=Category.objects.filter(slug='ssd'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('capacity',
                    'form_factor',
                    'language')

    list_display_links = ('form_factor',)

    list_filter = ('capacity',
                   'form_factor',
                   'language')

    fieldsets = (
        ('Абстрактная модель - Товары (общие данные)', {
            'fields': [
                ('category',
                 'slug'),
                ('title',
                 'company'),
                ('image',
                 'description',
                 'price')
            ]
        }),
        ('Общая информация', {
            'fields': ['market_launch_date']
        }),
        ('Основные', {
            'fields': [
                ('capacity',
                 'form_factor',
                 'interface'),
                ('chip_type_flash',
                 'controller'),
                ('m2_device_dimensions',
                 'recording_resource')
            ]
        }),
        ('Технические характеристики', {
            'fields': [
                ('buffer',
                 'hardware_encryption'),
                ('sequential_read_speed',
                 'sequential_write_speed'),
                ('average_random_read_speed',
                 'average_random_write_speed'),
                ('power_consumption_1',
                 'power_consumption_2'),
                ('time_between_failures',
                 'cooling',
                 'thickness')
            ]
        }),
        ('Комплектация', {
            'fields': ['adapter']
        }),
    )


@admin.register(HDD)
class HDDAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(queryset=Category.objects.filter(slug='hdd'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('drive_type',
                    'capacity',
                    'form_factor',
                    'language')

    list_display_links = ('drive_type',)

    list_filter = ('drive_type',
                   'capacity',
                   'form_factor',
                   'language')

    fieldsets = (
        ('Абстрактная модель - Товары (общие данные)', {
            'fields': [
                ('category',
                 'slug'),
                ('title',
                 'company'),
                ('image',
                 'description',
                 'price')
            ]
        }),
        ('Основные', {
            'fields': [
                ('drive_type',
                 'capacity',
                 'form_factor'),
                ('interface',
                 'spindle_speed')
            ]
        }),
        ('Технические характеристики', {
            'fields': [
                ('buffer',
                 'read_write_noise',
                 'standby_noise'),
                ('shock_during_operation',
                 'non_operation_shock'),
                ('power_consumption_1',
                 'power_consumption_2'),
                'thickness'
            ]
        }),
    )


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(queryset=Category.objects.filter(slug='cases'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('power_supply',
                    'type_of_case',
                    'language')

    list_display_links = ('power_supply',)

    list_filter = ('power_supply',
                   'type_of_case',
                   'language')

    fieldsets = (
        ('Абстрактная модель - Товары (общие данные)', {
            'fields': [
                ('category',
                 'slug'),
                ('title',
                 'company'),
                ('image',
                 'description',
                 'price')
            ]
        }),
        ('Общая информация', {
            'fields': [
                ('power_supply',
                 'type_of_case',
                 'game_case')
            ]
        }),
        ('Технические характеристики корпуса', {
            'fields': [
                ('case_color',
                 'case_material',
                 'transparent_window'),
                ('max_motherboard_size',
                 'compatible_motherboard',
                 'power_supply_loc'),
                ('fans_included',
                 'liquid_cooling_support',
                 'number_of_places_for_fans'),
                ('installed_coolers',
                 'noise_isolation',
                 'bays_5_inches'),
                ('external_bays_inches',
                 'internal_bays_inches',
                 'bays_2_inches'),
                ('remove_hard_drive_cage',
                 'screwless_drive_mounting',
                 'expansion_slots'),
                ('dust_filters',
                 'backlight_housing',
                 'backlight_controller'),
                ('fan_rotation_controller',
                 'max_video_card_length',
                 'max_cpu_cooler_height'),
                ('max_power_supply_length',
                 'vesa')
            ]
        }),
        ('Передняя панель корпуса', {
            'fields': [
                ('door',
                 'lock',
                 'info_display'),
                ('usb_2',
                 'usb_3_gen1_type_a_5gbit',
                 'usb_3_gen1_type_c_5gbit'),
                ('firewire',
                 'esata',
                 'hard_drive_docking_station'),
                ('cardreader',
                 'audio_output',
                 'micro_output')
            ]
        }),
        ('Габариты', {
            'fields': [
                ('height',
                 'width'),
                ('depth',
                 'weight')
            ]
        }),
    )


@admin.register(PowerSupply)
class PowerSupplyAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(queryset=Category.objects.filter(slug='powersupply'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('appointment',
                    'power',
                    'power_supply_standard',
                    'language')

    list_display_links = ('appointment',)

    list_filter = ('appointment',
                   'power',
                   'power_supply_standard',
                   'language')

    fieldsets = (
        ('Абстрактная модель - Товары (общие данные)', {
            'fields': [
                ('category',
                 'slug'),
                ('title',
                 'company'),
                ('image',
                 'description',
                 'price')
            ]
        }),
        ('Технические характеристики блока питания', {
            'fields': [
                ('appointment',
                 'power',
                 'power_supply_standard'),
                ('mains_input_voltage_range',
                 'number_of_separate_lines_12v'),
                ('max_line_current_12v',
                 'combined_load_12v'),
                ('power_factor_correction',
                 'efficiency',
                 'certificate_80_plus'),
                ('power_supply_fan_size',
                 'total_fans'),
                ('fan_illumination',
                 'case_illumination')
            ]
        }),
        ('Разъемы блока питания', {
            'fields': [
                ('power_cable_length',
                 'modular_power_cable_connection',
                 'motherboard_power'),
                ('cpu_4_pin',
                 'cpu_8_pin',
                 'fdd_4_pin',
                 'ide_4_pin'),
                ('sata',
                 'pcle_6_pin',
                 'pcle_8_pin',
                 'usb_power')
            ]
        }),
        ('Габариты', {
            'fields': [
                ('height',
                 'width'),
                ('depth',
                 'weight')
            ]
        }),
    )


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'cart',
                    'content_type',
                    'object_id')

    list_display_links = ('user',)

    fieldsets = (
        ('Информация', {
            'fields': [
                ('id',
                 'user',
                 'cart'),
                ('content_type',
                 'object_id',
                 'content_object'),
                ('quantity',
                 'final_price')
            ]
        }),
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('owner',
                    'total_products',
                    'final_price')

    list_display_links = ('owner',)

    fieldsets = (
        ('Информация', {
            'fields': [
                ('id',
                 'owner'),
                ('total_products',
                 'final_price')
            ]
        }),
    )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'phone',
                    'address')

    list_display_links = ('user',)

    fieldsets = (
        ('Информация о заказчике', {
            'fields': [
                ('id',
                 'user'),
                ('phone',
                 'address')
            ]
        }),
    )


@admin.register(TabIcons)
class TabIconsAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'info',)

    list_display_links = ('info',)

    fieldsets = (
        ('Информация', {
            'fields': [
                'id',
                'info'
            ]
        }),
    )
