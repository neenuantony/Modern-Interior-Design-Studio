# Generated by Django 4.2.4 on 2023-08-24 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0006_uploads'),
    ]

    operations = [
        migrations.CreateModel(
            name='select_checks_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('Kerala', 'KERALA'), ('Tamilnadu', 'TAMIL NADU'), ('Karnadaka', 'KARNADAKA'), ('Kashmir', 'KASHMIR'), ('Gujrat', 'GUJRAT')], max_length=30)),
                ('english', models.BooleanField(default=False)),
                ('malayalam', models.BooleanField(default=False)),
                ('hindi', models.BooleanField(default=False)),
            ],
        ),
    ]