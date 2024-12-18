# Generated by Django 5.1.4 on 2024-12-12 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_useraub_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='EtatBcmFluxSortants',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('banque', models.CharField(max_length=100)),
                ('nom_complet', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('devise', models.CharField(max_length=3)),
                ('type_transaction', models.CharField(max_length=10)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=20)),
                ('nature_economique', models.CharField(max_length=100)),
                ('identifiant_transaction', models.BigIntegerField()),
                ('nom_destinataire', models.CharField(max_length=200)),
                ('pays', models.CharField(max_length=100)),
                ('produit', models.CharField(max_length=100)),
                ('identifiant_banque', models.BigIntegerField()),
                ('commentaire', models.CharField(max_length=200)),
                ('taux_change', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type_message', models.CharField(max_length=10)),
                ('statut', models.IntegerField()),
            ],
            options={
                'db_table': 'ETATBCMFLUX_SORTANTS',
            },
        ),
        migrations.DeleteModel(
            name='EtatBcmFluxSortant',
        ),
    ]
