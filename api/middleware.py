# api/middleware.py
from django.db import connections

class DatabaseRouterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Récupérer l'URL de la demande
        path = request.path

        # Déterminer quelle base de données utiliser en fonction de l'URL
        if path.startswith('/api/get-flux-entrant/') or path.startswith('/api/get-flux-sortant/'):
            # Utiliser la base de données Oracle pour ces API
            using_db = 'oracle'
        else:
            # Utiliser la base de données SQLite par défaut pour les autres API
            using_db = 'sqlite'

        # Exécuter la vue avec la base de données appropriée
        with connections[using_db].cursor() as cursor:
            response = self.get_response(request)

        return response