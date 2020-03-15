# Generated by Django 3.0.3 on 2020-03-15 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('full_name', models.CharField(max_length=150, null=True, verbose_name='Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddConstraint(
            model_name='templatemodel',
            constraint=models.CheckConstraint(check=models.Q(full_name__length__lte=150), name='template-model-name-length'),
        ),
    ]
