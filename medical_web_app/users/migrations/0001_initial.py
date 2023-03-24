# Generated by Django 4.1.7 on 2023-03-22 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('schedule_date', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=50)),
                ('doc_email', models.EmailField(default='none@email.com', max_length=254)),
                ('approved', models.BooleanField(default=False, verbose_name='Aprroved')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('Email', models.EmailField(default='none@email.com', max_length=254)),
                ('first_name', models.CharField(default='', max_length=248)),
                ('Stomach_ache', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('Malaria', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('Injuries', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('Head_ache', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('Cough', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('Fever', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=248)),
                ('last_name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=50)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_physician', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]