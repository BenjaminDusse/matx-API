# Generated by Django 3.2.13 on 2022-09-09 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name']},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('cancel_order', 'Can cancel order')]},
        ),
        migrations.RemoveIndex(
            model_name='customer',
            name='store_custo_last_na_e6a359_idx',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
    ]