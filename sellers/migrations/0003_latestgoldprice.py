# Generated by Django 4.2.16 on 2025-03-11 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0002_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestGoldPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_id', models.IntegerField()),
                ('price', models.FloatField()),
                ('transaction_type', models.CharField(max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
