# Generated by Django 3.1.7 on 2021-04-03 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20210403_1405'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AndroidMetadata',
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='CatalogIeltsstories',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='Gmat',
        ),
        migrations.DeleteModel(
            name='Grammars',
        ),
        migrations.DeleteModel(
            name='Gramuse',
        ),
        migrations.DeleteModel(
            name='Gre',
        ),
        migrations.DeleteModel(
            name='Ielts',
        ),
        migrations.DeleteModel(
            name='Lessons',
        ),
        migrations.DeleteModel(
            name='Pronun',
        ),
        migrations.DeleteModel(
            name='PronunDetail',
        ),
        migrations.DeleteModel(
            name='Rules',
        ),
        migrations.DeleteModel(
            name='Vocabs',
        ),
    ]
