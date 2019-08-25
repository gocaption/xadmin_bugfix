# Generated by Django 2.2.4 on 2019-08-25 00:01

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlsLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=True, max_length=32, null=True, verbose_name='名称')),
            ],
            options={
                'verbose_name': '超级链接',
                'verbose_name_plural': '超级链接',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.PositiveSmallIntegerField(choices=[(0, 'BUG反馈'), (1, '意见建议'), (2, '讨论'), (3, '技术'), (4, '帮助'), (5, '公告')], verbose_name='主题分类')),
                ('publish_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='发帖时间')),
                ('update_time', models.DateTimeField(blank=True, null=True, verbose_name='更新时间')),
                ('view_count', models.PositiveSmallIntegerField(default=0, verbose_name='浏览次数')),
                ('title', models.CharField(help_text='字数限制在30个字以内', max_length=30, verbose_name='主题')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发布者')),
            ],
            options={
                'verbose_name': '畅所欲言',
                'verbose_name_plural': '畅所欲言',
            },
        ),
        migrations.CreateModel(
            name='AppUrlLink',
            fields=[
            ],
            options={
                'verbose_name': '快捷访问',
                'verbose_name_plural': '快捷访问',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('service.urlslink',),
        ),
        migrations.CreateModel(
            name='ReleaseLog',
            fields=[
            ],
            options={
                'verbose_name': '服务大厅',
                'verbose_name_plural': '服务大厅',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('service.article',),
        ),
        migrations.CreateModel(
            name='UnityAttentions',
            fields=[
            ],
            options={
                'verbose_name': '服务大厅',
                'verbose_name_plural': '服务大厅',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('service.article',),
        ),
        migrations.CreateModel(
            name='UnityHelper',
            fields=[
            ],
            options={
                'verbose_name': '服务大厅',
                'verbose_name_plural': '服务大厅',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('service.article',),
        ),
    ]
