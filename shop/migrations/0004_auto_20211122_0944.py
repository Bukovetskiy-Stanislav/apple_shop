# Generated by Django 3.2.7 on 2021-11-22 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20211119_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iphone',
            name='ram',
        ),
        migrations.RemoveField(
            model_name='macbook',
            name='diagonal',
        ),
        migrations.RemoveField(
            model_name='macbook',
            name='display_type',
        ),
        migrations.RemoveField(
            model_name='macbook',
            name='processor_freq',
        ),
        migrations.RemoveField(
            model_name='macbook',
            name='ram',
        ),
        migrations.RemoveField(
            model_name='macbook',
            name='time_without_charge',
        ),
        migrations.RemoveField(
            model_name='macbook',
            name='video',
        ),
        migrations.AddField(
            model_name='iphone',
            name='storage',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=' встраивамой памяти'),
        ),
        migrations.AddField(
            model_name='macbook',
            name='audio',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Audio'),
        ),
        migrations.AddField(
            model_name='macbook',
            name='battery_and_power',
            field=models.TextField(blank=True, max_length=255, verbose_name='Battery and Power'),
        ),
        migrations.AddField(
            model_name='macbook',
            name='camera',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Camera'),
        ),
        migrations.AddField(
            model_name='macbook',
            name='charging',
            field=models.TextField(blank=True, max_length=255, verbose_name='Charg\xading and Expan\xadsion'),
        ),
        migrations.AddField(
            model_name='macbook',
            name='chip',
            field=models.TextField(blank=True, max_length=255, verbose_name='Chip'),
        ),
        migrations.AddField(
            model_name='macbook',
            name='color',
            field=models.TextField(blank=True, max_length=200, verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='macbook',
            name='display',
            field=models.TextField(blank=True, max_length=255, verbose_name='Display'),
        ),
        migrations.AddField(
            model_name='macbook',
            name='keyboard_and_trackpad',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Key\xadboard and Track\xadpad'),
        ),
        migrations.AddField(
            model_name='macbook',
            name='memory',
            field=models.TextField(blank=True, max_length=255, verbose_name='Memory'),
        ),
        migrations.AddField(
            model_name='macbook',
            name='size_and_weight',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Size and Weight'),
        ),
        migrations.AddField(
            model_name='macbook',
            name='storage',
            field=models.TextField(blank=True, max_length=255, verbose_name='Storage'),
        ),
        migrations.AddField(
            model_name='macbook',
            name='toch_id',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Touch ID'),
        ),
        migrations.AddField(
            model_name='macbook',
            name='video_support',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Video Support'),
        ),
        migrations.AddField(
            model_name='macbook',
            name='wireless',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Wireless'),
        ),
        migrations.AlterField(
            model_name='iphone',
            name='battery',
            field=models.TextField(blank=True, max_length=255, verbose_name='Power and Battery'),
        ),
        migrations.AlterField(
            model_name='iphone',
            name='frontal_cam_mp',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Фронтальная камера'),
        ),
        migrations.AlterField(
            model_name='iphone',
            name='interfaces',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Interfaces'),
        ),
        migrations.AlterField(
            model_name='iphone',
            name='main_cam_mp',
            field=models.TextField(max_length=1000, verbose_name='Главная камера'),
        ),
        migrations.AlterField(
            model_name='iphone',
            name='memory',
            field=models.CharField(max_length=255, verbose_name='Оперативная память'),
        ),
        migrations.AlterField(
            model_name='iphone',
            name='sensors',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Sensors'),
        ),
        migrations.AlterField(
            model_name='iphone',
            name='sim_card',
            field=models.TextField(blank=True, max_length=255, verbose_name='SIM Card'),
        ),
        migrations.AlterField(
            model_name='iphone',
            name='weight',
            field=models.TextField(blank=True, max_length=255, verbose_name='Size and Weight'),
        ),
        migrations.AlterField(
            model_name='iphone',
            name='wireless',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Cellular and Wireless'),
        ),
    ]