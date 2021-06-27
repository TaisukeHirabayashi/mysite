# Generated by Django 3.0.2 on 2021-06-27 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grades', models.CharField(max_length=10, verbose_name='学年一覧')),
            ],
            options={
                'verbose_name_plural': '学年モデル',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='名前')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Grade', verbose_name='学年を選択してください')),
            ],
            options={
                'verbose_name_plural': 'メンバーモデル',
            },
        ),
    ]