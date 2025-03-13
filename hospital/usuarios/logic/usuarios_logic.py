from ..models import Usuario

def get_usuarios():
    usuarios = Usuario.objects.all()
    return usuarios

def get_usuario(user_pk):
    usuario = Usuario.objects.get(pk=user_pk)
    return usuario

def update_usuario(user_pk, new_user):
    usuario = get_usuario(user_pk)
    usuario.name = new_user["name"]
    usuario.save()
    return usuario

def create_usuario(user):
    usuario = Usuario(name=user["name"])
    usuario.save()
    return usuario