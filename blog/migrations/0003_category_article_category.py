# Generated by Django 5.0.6 on 2024-05-30 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=30)),
                ('creat', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='blog.category'),
        ),
    ]
