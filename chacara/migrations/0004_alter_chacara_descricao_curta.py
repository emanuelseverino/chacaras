# Generated by Django 4.0.3 on 2022-03-16 18:18

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('chacara', '0003_chacara_data_add_chacara_descricao_curta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chacara',
            name='descricao_curta',
            field=tinymce.models.HTMLField(max_length=300),
        ),
    ]
