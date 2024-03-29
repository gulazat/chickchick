# Generated by Django 3.0.7 on 2021-10-21 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_title', models.CharField(blank=True, max_length=128, null=True, verbose_name='视频分类')),
            ],
            options={
                'db_table': 'A_category',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('T_tag', models.CharField(max_length=128, verbose_name='视频标签')),
            ],
            options={
                'db_table': 'C_tag',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.CharField(blank=True, max_length=255, null=True)),
                ('file', models.FileField(max_length=255, upload_to='')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='cover/')),
                ('view_count', models.IntegerField(blank=True, default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True, max_length=20)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='video.Category')),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='video.Tag')),
            ],
            options={
                'db_table': 'C_video',
            },
        ),
    ]
