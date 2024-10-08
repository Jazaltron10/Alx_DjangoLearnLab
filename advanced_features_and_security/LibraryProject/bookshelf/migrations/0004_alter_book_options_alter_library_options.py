# Generated by Django 5.1 on 2024-08-23 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0003_rename_profile_picture_customuser_profile_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_view_book', 'Can view book'), ('can_add_book', 'Can add book'), ('can_change_book', 'Can change book'), ('can_delete_book', 'Can delete book')]},
        ),
        migrations.AlterModelOptions(
            name='library',
            options={'permissions': [('can_view_library', 'Can view library'), ('can_add_library', 'Can add library'), ('can_change_library', 'Can change library'), ('can_delete_library', 'Can delete library')]},
        ),
    ]
