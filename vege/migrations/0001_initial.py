# Generated by Django 5.0.3 on 2024-05-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rec_name', models.CharField(max_length=100)),
                ('Rec_desription', models.TextField()),
                ('Rec_img', models.ImageField(upload_to='receipes')),
            ],
        ),
    ]
