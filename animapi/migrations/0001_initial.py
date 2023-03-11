# Generated by Django 4.1.7 on 2023-03-11 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('release', models.CharField(max_length=50)),
                ('recommended', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Watcher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist_Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animapi.anime')),
                ('watcher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_watchlist', to='animapi.watcher')),
            ],
        ),
        migrations.AddField(
            model_name='anime',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animapi.genre'),
        ),
    ]
