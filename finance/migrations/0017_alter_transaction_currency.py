# Generated by Django 4.2.3 on 2023-07-30 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0016_alter_transaction_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='currency',
            field=models.ForeignKey(default='pln', on_delete=django.db.models.deletion.DO_NOTHING, related_name='dashboard', to='finance.currency'),
        ),
    ]
