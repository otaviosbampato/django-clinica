from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("medical", "0002_especialidade_alter_consulta_options_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Especialidade",
        ),
    ]
