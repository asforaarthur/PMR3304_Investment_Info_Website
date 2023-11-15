from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0002_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('investment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='investments.investment')),
                ('service', models.CharField(blank=True, max_length=255)),
                ('has_flat_price', models.BooleanField(default=False)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
        ),
    ]
