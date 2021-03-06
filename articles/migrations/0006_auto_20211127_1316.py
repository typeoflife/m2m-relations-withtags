# Generated by Django 3.2.9 on 2021-11-27 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_scope'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scopeposition',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='scopeposition',
            name='scope',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position', to='articles.scope'),
        ),
    ]
