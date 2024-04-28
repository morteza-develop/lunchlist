# Generated by Django 5.0.4 on 2024-04-28 16:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodName', models.CharField(max_length=100, verbose_name='نام غذا')),
                ('description', models.CharField(max_length=250, verbose_name='توضیحات')),
                ('price', models.IntegerField(null=True, verbose_name='قیمت غذا')),
                ('foodType', models.IntegerField(choices=[(1, 'صبحانه'), (2, 'نهار')], default=0, verbose_name='نوع غذا')),
                ('foodImage', models.ImageField(blank=True, upload_to='static/images/', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'غذا',
                'verbose_name_plural': 'غذاها',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام منو')),
                ('createDate', models.DateField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('expire', models.DateField(verbose_name='زمان انقضاء')),
                ('status', models.IntegerField(choices=[(0, 'بسته'), (1, 'باز')], default=0, verbose_name='وضعیت منو')),
            ],
            options={
                'verbose_name': 'منو',
                'verbose_name_plural': 'منو ها',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileimage', models.ImageField(upload_to='static/images/', verbose_name='تصویر')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.food', verbose_name='انتخاب غذا')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.menu', verbose_name='انتخاب منو')),
            ],
            options={
                'verbose_name': 'آیتمهای منو',
                'verbose_name_plural': 'آیتمهای منو',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.food', verbose_name='غذا')),
                ('menuItem', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.menuitem', verbose_name='منو')),
                ('userName', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'رزرو',
                'verbose_name_plural': 'رزروهای انجام شده',
            },
        ),
    ]
