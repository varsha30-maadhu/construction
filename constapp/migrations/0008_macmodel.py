# Generated by Django 4.1.6 on 2023-02-05 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constapp', '0007_wishmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='macmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='constapp/static')),
                ('nmac', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('per', models.CharField(choices=[('HOUR', 'HOUR'), ('MINUTE', 'MINUTE')], max_length=50)),
                ('des', models.CharField(max_length=500)),
            ],
        ),
    ]