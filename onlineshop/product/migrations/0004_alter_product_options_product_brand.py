# Generated by Django 4.2.2 on 2023-08-09 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('date_added',)},
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=255, null=True),
        ),
    ]