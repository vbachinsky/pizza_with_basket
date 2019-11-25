# Generated by Django 2.2.7 on 2019-11-25 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_card_indicator', models.BooleanField(default=False)),
                ('client_deposit', models.BooleanField(default=False)),
                ('date_enroller', models.DateField(auto_now_add=True)),
                ('date_terminate', models.DateField()),
            ],
            options={
                'verbose_name': 'Client account',
                'verbose_name_plural': 'Client accounts',
            },
        ),
        migrations.CreateModel(
            name='Dough',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='InstancePizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True)),
                ('pizzas', models.ManyToManyField(related_name='order_template', to='dj_pizzas.InstancePizza')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('adress', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Snacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
            options={
                'verbose_name_plural': 'Snacks',
            },
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('dough', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dj_pizzas.Dough')),
                ('topping', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dj_pizzas.Topping')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.IntegerField()),
                ('order', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dj_pizzas.Order')),
            ],
            options={
                'verbose_name': 'Ordered payment',
                'verbose_name_plural': 'Ordered payments',
            },
        ),
        migrations.CreateModel(
            name='OrderedSnacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dj_pizzas.Order')),
                ('snack', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dj_pizzas.Snacks')),
            ],
            options={
                'verbose_name': 'Ordered snacks',
                'verbose_name_plural': 'Ordered snacks',
            },
        ),
        migrations.AddField(
            model_name='instancepizza',
            name='pizza_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pizza_template', to='dj_pizzas.Pizza'),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_tax', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('employee_job_category', models.CharField(max_length=100)),
                ('person', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dj_pizzas.Person')),
            ],
        ),
        migrations.CreateModel(
            name='ClientTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('sales_tax', models.FloatField(default=0.05)),
                ('client_account', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dj_pizzas.ClientAccount')),
                ('employee', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dj_pizzas.Employee')),
            ],
            options={
                'verbose_name': 'Client transaction',
                'verbose_name_plural': 'Client transactions',
            },
        ),
        migrations.CreateModel(
            name='ClientAccountPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_account', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dj_pizzas.ClientAccount')),
                ('person', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dj_pizzas.Person')),
            ],
            options={
                'verbose_name': 'Client account person',
                'verbose_name_plural': 'Client accounts persons',
            },
        ),
    ]