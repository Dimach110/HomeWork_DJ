# Generated by Django 4.1.1 on 2022-09-20 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_scope_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['is_main'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
