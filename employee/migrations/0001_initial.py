# Generated by Django 4.0.5 on 2022-07-15 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('reg_name', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('bank', models.CharField(max_length=20)),
                ('bank_num', models.CharField(max_length=30)),
                ('inwork', models.DateField()),
                ('department', models.CharField(max_length=30)),
                ('rank', models.CharField(max_length=30)),
                ('worksystem', models.IntegerField()),
                ('pay', models.IntegerField()),
                ('insurance', models.CharField(max_length=20)),
                ('health', models.CharField(max_length=30)),
                ('content', models.TextField()),
            ],
        ),
    ]
