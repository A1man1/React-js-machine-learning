# Generated by Django 3.0.7 on 2020-07-10 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='topic',
            field=models.CharField(blank=True, default='electroic science', max_length=100),
        ),
    ]
