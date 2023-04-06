# Generated by Django 4.1.7 on 2023-02-25 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estimate', '0007_scope_direct_cost_scope_equipment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qty', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('unit', models.CharField(default='lot', max_length=20)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('scope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='estimate.scope')),
            ],
        ),
    ]