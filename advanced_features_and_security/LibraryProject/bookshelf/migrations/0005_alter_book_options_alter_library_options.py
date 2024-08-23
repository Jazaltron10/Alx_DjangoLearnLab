# Generated by Django 5.1 on 2024-08-23 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0004_alter_book_options_alter_library_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_view_book', 'Can view book'), ('can_create_book', 'Can create book'), ('can_change_book', 'Can change book'), ('can_delete_book', 'Can delete book')]},
        ),
        migrations.AlterModelOptions(
            name='library',
            options={'permissions': [('can_view_library', 'Can view library'), ('can_create_library', 'Can create library'), ('can_change_library', 'Can change library'), ('can_delete_library', 'Can delete library')]},
        ),
    ]
