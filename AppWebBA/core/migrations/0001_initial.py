# Generated by Django 3.2.4 on 2022-06-22 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaestroProducto',
            fields=[
                ('idp', models.IntegerField(primary_key=True, serialize=False)),
                ('nomprod', models.CharField(max_length=100)),
                ('descprod', models.CharField(max_length=300)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MaestroUsuario',
            fields=[
                ('rut', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('tipousu', models.CharField(max_length=50)),
                ('nomusu', models.CharField(max_length=100)),
                ('apeusu', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('dirusu', models.CharField(max_length=300)),
                ('pwd', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WebFactura',
            fields=[
                ('nrofac', models.IntegerField(primary_key=True, serialize=False)),
                ('fechafac', models.DateField()),
                ('descfac', models.CharField(max_length=300)),
                ('monto', models.IntegerField()),
                ('idp', models.ForeignKey(db_column='idp', on_delete=django.db.models.deletion.DO_NOTHING, to='core.maestroproducto')),
                ('rutcli', models.ForeignKey(db_column='rutcli', on_delete=django.db.models.deletion.DO_NOTHING, to='core.maestrousuario')),
            ],
        ),
        migrations.CreateModel(
            name='WebSolicitudServicio',
            fields=[
                ('nross', models.IntegerField(primary_key=True, serialize=False)),
                ('tiposs', models.CharField(max_length=50)),
                ('fechavisita', models.DateField()),
                ('descss', models.CharField(max_length=200)),
                ('estadoss', models.CharField(max_length=50)),
                ('nrofac', models.ForeignKey(db_column='nrofac', on_delete=django.db.models.deletion.DO_NOTHING, to='core.webfactura')),
                ('ruttec', models.ForeignKey(db_column='ruttec', on_delete=django.db.models.deletion.DO_NOTHING, to='core.maestrousuario')),
            ],
        ),
        migrations.CreateModel(
            name='BodegaStockProducto',
            fields=[
                ('idb', models.IntegerField(primary_key=True, serialize=False)),
                ('idp', models.ForeignKey(db_column='idp', on_delete=django.db.models.deletion.DO_NOTHING, to='core.maestroproducto')),
                ('nrofac', models.ForeignKey(blank=True, db_column='nrofac', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.webfactura')),
            ],
        ),
        migrations.CreateModel(
            name='BodegaGuiaDespacho',
            fields=[
                ('nrogd', models.IntegerField(primary_key=True, serialize=False)),
                ('estadogd', models.CharField(max_length=50)),
                ('idp', models.ForeignKey(db_column='idp', on_delete=django.db.models.deletion.DO_NOTHING, to='core.maestroproducto')),
                ('nrofac', models.ForeignKey(db_column='nrofac', on_delete=django.db.models.deletion.DO_NOTHING, to='core.webfactura')),
            ],
        ),
    ]
