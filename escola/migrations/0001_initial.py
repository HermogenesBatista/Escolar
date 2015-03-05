# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=150)),
                ('cnpj', models.CharField(max_length=15)),
                ('rua', models.CharField(max_length=150)),
                ('num_rua', models.CharField(max_length=10)),
                ('bairro_rua', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=30)),
                ('codInep', models.IntegerField(max_length=10)),
                ('tel_principal', models.CharField(max_length=16)),
                ('tel_alternativo', models.CharField(max_length=16)),
                ('situacao', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Escolaridade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('situacao', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('situacao', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Permissoes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('situacao', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=150)),
                ('pai', models.CharField(max_length=150)),
                ('mae', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=12)),
                ('rg', models.CharField(max_length=25)),
                ('org_exp', models.CharField(max_length=10)),
                ('dt_nasc', models.DateField()),
                ('rua', models.CharField(max_length=150)),
                ('num_rua', models.CharField(max_length=10)),
                ('bairro_rua', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=30)),
                ('tel_principal', models.CharField(max_length=16)),
                ('tel_alternativo', models.CharField(max_length=16)),
                ('situacao', models.BooleanField(default=True)),
                ('escolaridade', models.ForeignKey(to='escola.Escolaridade')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoEntidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('situacao', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoVida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('situacao', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='responsavel',
            name='tipo_vida',
            field=models.ForeignKey(to='escola.TipoVida'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='perfil',
            name='permissao',
            field=models.ManyToManyField(to='escola.Permissoes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entidade',
            name='responsavel',
            field=models.ManyToManyField(to='escola.Responsavel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entidade',
            name='tipo_entidade',
            field=models.ForeignKey(to='escola.TipoEntidade'),
            preserve_default=True,
        ),
    ]
