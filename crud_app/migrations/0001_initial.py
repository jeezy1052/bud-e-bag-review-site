# Generated by Django 4.0.1 on 2022-01-22 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('strain', models.CharField(max_length=100)),
                ('consumpition_method', models.CharField(choices=[('Smokeable', 'Smokeable'), ('Vape Pen', 'Vape Pen')], default='Smokeable Medicine', max_length=25)),
                ('is_skunk_one', models.BooleanField(default=False, verbose_name='Is Skunk')),
                ('is_harsh_two', models.BooleanField(default=False, verbose_name='Is Harsh (Snicklefritz)')),
                ('is_fire_three', models.BooleanField(default=False, verbose_name='Is Fire(Killer Strain)')),
                ('is_hall_of_fame_four', models.BooleanField(default=False, verbose_name='Is Hall Of Fame Strains')),
                ('review', models.TextField(blank=None, null=True)),
            ],
        ),
    ]