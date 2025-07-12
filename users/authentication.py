# /users/authentication.py

from mozilla_django_oidc.auth import OIDCAuthenticationBackend

class MyOIDCAB(OIDCAuthenticationBackend):
    def create_user(self, claims):
        """
        Sobrescribe el método original para crear usuarios,
        usando TODOS los claims (datos) que vienen de Keycloak.
        """
        user = self.UserModel.objects.create_user(
            username=claims.get('given_name'),  # 'sub' es el ID único de Keycloak
            email=claims.get('email'),
            first_name=claims.get('given_name'),
            last_name=claims.get('family_name'),
            cedula=claims.get('cedula') 
        )

        return user