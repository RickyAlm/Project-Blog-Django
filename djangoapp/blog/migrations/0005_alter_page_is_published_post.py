# Generated by Django 4.2.1 on 2023-06-07 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_page_options_alter_page_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='is_published',
            field=models.BooleanField(default=False, help_text='This field must be checked in order for the page to be publicly displayed.'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('slug', models.SlugField(blank=True, default=None, max_length=70, null=True, unique=True)),
                ('is_published', models.BooleanField(default=False, help_text='If checked, it will display the cover inside the post.')),
                ('content', models.TextField()),
                ('cover', models.ImageField(blank=True, default='', upload_to='posts_%Y/%m/')),
                ('cover_in_post_content', models.BooleanField(default=True, help_text='If checked, it will display the cover inside the post.')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
                ('tags', models.ManyToManyField(blank=True, default='', to='blog.tag')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
