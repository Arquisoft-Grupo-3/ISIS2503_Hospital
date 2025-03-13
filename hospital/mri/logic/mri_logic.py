from collections import Counter
from django.db.models import Count
from ..models import MRI, Usuario

def map_reduce_usuarios():
    # MAP: Extraemos solo los IDs de los usuarios atendidos
    usuarios_ids = MRI.objects.values_list('usuario', flat=True)

    # REDUCE: Contamos cuántas veces aparece cada usuario_id
    conteo_usuarios = Counter(usuarios_ids)

    # Ordenamos de mayor a menor frecuencia
    usuarios_ordenados = sorted(conteo_usuarios.items(), key=lambda item: item[1], reverse=True)

    return usuarios_ordenados

def get_usuario_mas_atendido():
    usuarios_ordenados = map_reduce_usuarios()

    if usuarios_ordenados:
        user_id, cantidad = usuarios_ordenados[0]  # Usuario con más atenciones
        usuario = Usuario.objects.get(id=user_id)
        return {"usuario": usuario, "cantidad": cantidad}
    return None
