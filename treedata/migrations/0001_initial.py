# Generated by Django 4.1.1 on 2022-12-11 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('left_child', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='left_parent', to='treedata.accounttwo')),
                ('right_child', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='right_parent', to='treedata.accounttwo')),
            ],
        ),
        migrations.CreateModel(
            name='AccountThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='child', to='treedata.accountthree')),
            ],
        ),
        migrations.CreateModel(
            name='AccountOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('left_child', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='left_parent', to='treedata.accountone')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='child', to='treedata.accountone')),
                ('right_child', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='right_parent', to='treedata.accountone')),
            ],
        ),
    ]
