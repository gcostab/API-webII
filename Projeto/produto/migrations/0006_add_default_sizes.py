from django.db import migrations

def add_default_sizes(apps, schema_editor):
    Tamanho = apps.get_model('produto', 'Tamanho')
    sizes = [
        ('PP', 'Piquenique'),
        ('P', 'Pequeno'),
        ('M', 'Medio'),
        ('G', 'Grande'),
        ('GG', 'Gigante'),
        ('XG', 'XGigante'),
        ('XXG', 'XXGigante'),
        ('XXXG', 'XXXGigante'),
    ]
    for size in sizes:
        Tamanho.objects.create(tamanho=size[0])

class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_tamanho_remove_produto_tamanho_produto_tamanho'),
    ]

    operations = [
        migrations.RunPython(add_default_sizes),
    ]
