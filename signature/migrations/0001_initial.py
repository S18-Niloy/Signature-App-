# Generated by Django 5.1.4 on 2024-12-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_image', models.ImageField(upload_to='originals/')),
                ('uploaded_image', models.ImageField(upload_to='uploads/')),
                ('result', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
