# Generated by Django 4.1 on 2022-11-26 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='meta_description',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_keywords',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='fname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='lname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_mode',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out For Shipping', 'Out For Shipping'), ('Completed', 'Completed')], default='Pending', max_length=25),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='tracking_no',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_description',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_keywords',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='product',
            name='original_price',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pincode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(max_length=20),
        ),
    ]
