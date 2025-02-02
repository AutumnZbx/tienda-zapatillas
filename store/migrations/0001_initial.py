# Generated by Django 4.1.2 on 2024-06-28 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_cat', models.AutoField(db_column='id_cat', primary_key=True, serialize=False)),
                ('nombre_cat', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_marca', models.AutoField(db_column='id_marca', primary_key=True, serialize=False)),
                ('nombre_marca', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id_tag', models.AutoField(db_column='id_tag', primary_key=True, serialize=False)),
                ('nombre_tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(db_column='id_producto', primary_key=True, serialize=False)),
                ('nombre_prod', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=300)),
                ('imagen', models.ImageField(null=True, upload_to='')),
                ('cantidad', models.IntegerField()),
                ('disponible', models.BooleanField(default=True)),
                ('id_cat', models.ForeignKey(db_column='id_cat', on_delete=django.db.models.deletion.CASCADE, to='store.categoria')),
                ('id_marca', models.ForeignKey(db_column='id_marca', on_delete=django.db.models.deletion.CASCADE, to='store.marca')),
                ('tags', models.ManyToManyField(to='store.tag')),
            ],
            options={
                'ordering': ['id_marca'],
            },
        ),
    ]
