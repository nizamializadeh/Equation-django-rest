# Generated by Django 4.0.5 on 2022-06-16 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equation', '0002_remove_equation_example_example_equation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='equation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='equation.equation'),
        ),
    ]