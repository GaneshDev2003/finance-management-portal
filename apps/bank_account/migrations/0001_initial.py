# Generated by Django 4.0.5 on 2022-06-15 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionType', models.CharField(max_length=50)),
                ('transactoinPurpose', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountNumber', models.CharField(max_length=50)),
                ('accountType', models.CharField(max_length=50)),
                ('transactions', models.ManyToManyField(to='bank_account.transaction')),
            ],
        ),
    ]
