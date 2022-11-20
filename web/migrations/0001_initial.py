# Generated by Django 3.1.7 on 2021-03-31 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('detailDiscription', models.TextField(null=True)),
                ('place', models.CharField(max_length=300, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(upload_to='web')),
                ('twoimage', models.ImageField(default='default.jpg', upload_to='web')),
                ('threeimage', models.ImageField(default='default.jpg', upload_to='web')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
