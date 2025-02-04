from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('product_type', models.CharField(choices=[('F', 'Fruit'), ('V', 'Vegetable')], max_length=25)),
                ('price', models.PositiveIntegerField()),
                ('img', models.ImageField(upload_to='')),
                ('origin', models.CharField(max_length=120)),
                ('quantity', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('availibility', models.BooleanField(default=True)),
                ('quantity_per_order', models.PositiveIntegerField()),
                ('date_added', models.DateField()),
            ],
        ),
    ]
