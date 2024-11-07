# capa de servicio/lógica de negocio
from ..transport import transport
from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user


def getAllImages(input=None):
    # obtiene un listado de datos "crudos" desde la API, usando a transport.py.
    # brindamos a un valor a la variable para usarlo en un futuro programa
    json_collection = transport.getAllImages()

    # recorre cada dato crudo de la colección anterior, lo convierte en una Card y lo agrega a images.
    images = []
    # programa que recorre los archivos de json_collection y los convierte en cards que se mostraran en la pagina
    for i in range(len(json_collection)):
        image = translator.fromRequestIntoCard(json_collection[i])
        images.append(image)

    return images

# añadir favoritos (usado desde el template 'home.html')


def saveFavourite(request):
    fav = ''  # transformamos un request del template en una Card.
    fav.user = ''  # le asignamos el usuario correspondiente.

    return repositories.saveFavourite(fav)  # lo guardamos en la base.

# usados desde el template 'favourites.html'


def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').
        favourite_list = []
        mapped_favourites = []

        for favourite in favourite_list:
            # transformamos cada favorito en una Card, y lo almacenamos en card.
            card = ''
            mapped_favourites.append(card)

        return mapped_favourites


def deleteFavourite(request):
    favId = request.POST.get('id')
    # borramos un favorito por su ID.
    return repositories.deleteFavourite(favId)
