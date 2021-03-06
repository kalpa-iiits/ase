

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rmp', '0001_initial'),
        ('shoppingPortalApp', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(max_length=15)),
                ('patient_name', models.CharField(max_length=15, null=True)),
                ('patient_phno', models.IntegerField(null=True)),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('deliver_addr_houseno', models.CharField(max_length=30, null=True)),
                ('deliver_addr_street', models.CharField(max_length=30, null=True)),
                ('deliver_addr_pincode', models.IntegerField(null=True)),
                ('deliver_addr_district', models.CharField(max_length=20, null=True)),
                ('deliver_addr_state', models.CharField(max_length=15, null=True)),
                ('deliver_addr_country', models.CharField(max_length=15, null=True)),
                ('payment_method', models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('Pay Online', 'Pay Online')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='shoppingPortalApp.medicine')),
                ('is_ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('date_ordered', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='shopping_cart.OrderItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rmp.rmpContact'),
        ),
    ]
