# Generated by Django 3.2.6 on 2023-09-14 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0002_newsletter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='newsletter',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
