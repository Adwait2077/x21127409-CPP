# Generated by Django 2.2 on 2020-07-30 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(choices=[('SPAM', 'SPAM'), ('INAPPROPRIATE', 'INAPPROPRIATE')], max_length=10)),
                ('date_reported', models.DateTimeField(default=django.utils.timezone.now)),
                ('reported_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_user', to=settings.AUTH_USER_MODEL)),
                ('reporting_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporting_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25)),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('description', models.CharField(blank=True, max_length=100)),
                ('wing', models.CharField(blank=True, choices=[('ARMY', 'ARMY'), ('NAVAL', 'NAVAL'), ('AIR FORCE', 'AIR FORCE')], max_length=10)),
                ('camps', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('followers', models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('follows', models.ManyToManyField(blank=True, related_name='follows', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
