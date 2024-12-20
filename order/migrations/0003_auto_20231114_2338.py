# Generated by Django 3.2 on 2023-11-14 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_review_updata_dt'),
        ('order', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_detail',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RemoveField(
            model_name='order_detail',
            name='address',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='pay',
            field=models.CharField(choices=[('a', '계좌이체'), ('b', '무통장 입금'), ('c', '카드')], default='a', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='request',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='order_detail',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_dt',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_dt',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
