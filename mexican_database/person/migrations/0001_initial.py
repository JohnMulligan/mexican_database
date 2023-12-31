# Generated by Django 5.0 on 2023-12-06 00:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("document", "0001_initial"),
        ("geo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CalidadDePersona",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="CategoriaDeOcupacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="EstatusDeEsclavizador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Etonimo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="HispanizacionDePersona",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Ocupacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="RolDeRelacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Sexo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="SituacionDeLugarDeEsclavizador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="TipoDeRelacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="PersonaEsclavizada",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("primer_nombre", models.CharField(max_length=50)),
                ("apellido", models.CharField(max_length=50)),
                ("nombre_y_apellido_estandarizados", models.CharField(max_length=100)),
                ("cabella", models.CharField(max_length=100)),
                ("ojos", models.CharField(max_length=100)),
                ("marcas_corporales", models.CharField(max_length=100)),
                (
                    "registros_de_conductas_y_condiciones",
                    models.CharField(max_length=350),
                ),
                ("notes", models.CharField(blank=True, max_length=8192, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                (
                    "calidad_de_persona",
                    models.ManyToManyField(to="person.calidaddepersona"),
                ),
                (
                    "categoria_de_ocupacion",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="person.categoriadeocupacion",
                    ),
                ),
                (
                    "etonimo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="person.etonimo",
                    ),
                ),
                (
                    "hispanizacion",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="person.hispanizaciondepersona",
                    ),
                ),
                (
                    "lugar_nuevo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="geo.lugar",
                    ),
                ),
                (
                    "lugar_ultimo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="geo.lugar",
                    ),
                ),
                (
                    "ocupacion",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="person.ocupacion",
                    ),
                ),
                ("procedencia", models.ManyToManyField(to="geo.lugar")),
                (
                    "sexo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="person.sexo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Esclavizador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("apellido", models.CharField(max_length=50)),
                (
                    "calidad_de_persona",
                    models.ManyToManyField(to="person.calidaddepersona"),
                ),
                (
                    "categoria_de_ocupacion",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="person.categoriadeocupacion",
                    ),
                ),
                (
                    "lugar",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="geo.lugar",
                    ),
                ),
                (
                    "estatus_de_esclavizador",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="person.estatusdeesclavizador",
                    ),
                ),
                (
                    "ocupacion",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="person.ocupacion",
                    ),
                ),
                (
                    "sexo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="person.sexo",
                    ),
                ),
                (
                    "lugar_situacion",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="person.situaciondelugardeesclavizador",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EsclavizadorDocumentoConexion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "persona_edad",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Edad registrada en el documento",
                    ),
                ),
                (
                    "persona_altura",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Altura registrada en el documento",
                    ),
                ),
                (
                    "documento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="documento_eslclavizador_conexiones",
                        to="document.documento",
                    ),
                ),
                (
                    "personas_esclavizadas",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="personas_esclavizadas_relaciones",
                        to="person.personaesclavizada",
                    ),
                ),
                (
                    "rol_de_esclavizador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="person.rolderelacion",
                    ),
                ),
                (
                    "tipo_de_relacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="person.tipoderelacion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EsclavizadaDocumentoConexion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "persona_edad",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Edad registrada en el documento",
                    ),
                ),
                (
                    "persona_altura",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Altura registrada en el documento",
                    ),
                ),
                (
                    "documento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="documento_esclavizada_conexiones",
                        to="document.documento",
                    ),
                ),
                (
                    "persona_esclavizadas",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="persona_esclavizadas_relaciones",
                        to="person.personaesclavizada",
                    ),
                ),
                (
                    "tipo_de_relacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="person.tipoderelacion",
                    ),
                ),
            ],
        ),
    ]
