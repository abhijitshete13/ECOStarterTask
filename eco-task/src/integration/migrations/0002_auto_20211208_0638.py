# Generated by Django 3.2.9 on 2021-12-08 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integration',
            name='activity',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='businessDbaName',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='businessEmail',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='businessLegalName',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='businessOwnerName',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='businessPhone',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='businessStructure',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='expirationDate',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='issueDate',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='licenseDesignation',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='licenseNumber',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='licenseStatus',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='licenseStatusDate',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='integration',
            name='licenseTerm',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='licenseType',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='licensingAuthority',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='licensingAuthorityId',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='parcelNumber',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='premiseCity',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='premiseCounty',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='premiseState',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='premiseStreetAddress',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='integration',
            name='premiseZipCode',
            field=models.CharField(max_length=225),
        ),
    ]
