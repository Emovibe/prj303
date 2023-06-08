# Generated by Django 4.2 on 2023-05-14 01:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('token_expiration_time', models.DateTimeField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songTitle', models.CharField(max_length=255)),
                ('singer', models.CharField(max_length=355)),
                ('img', models.ImageField(upload_to='music')),
                ('audio_file', models.FileField(upload_to='music', validators=[django.core.validators.FileExtensionValidator(['mp3', 'wav', 'ogg', 'm4a', 'flac', 'aac', 'wma', 'aiff', 'alac', 'opus', 'mp4'])])),
                ('category', models.CharField(choices=[('happy', 'Happy'), ('sad', 'Sad'), ('disgust', 'Disgust'), ('angry', 'Angry'), ('surprise', 'Surprise'), ('neutral', 'Neutral'), ('fear', 'Fear')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]