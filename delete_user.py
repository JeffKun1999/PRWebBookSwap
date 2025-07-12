# delete_user.py
import os
import sys
import django

# --- Configuración del Entorno de Django ---
# Asegúrate de que la siguiente línea apunte a tu archivo settings.py
# 'backend.settings' es el nombre de la carpeta del proyecto + .settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings') 
django.setup()
# ---------------------------------------------

# Importa tu modelo de usuario personalizado
from users.models import CustomUser

def delete_user_by_cedula(cedula):
    """
    Busca un usuario por su cédula y lo elimina si existe.
    """
    try:
        # Busca al usuario que coincida con la cédula proporcionada
        user_to_delete = CustomUser.objects.get(cedula=cedula)
        
        print(f"✅ Usuario encontrado: {user_to_delete.username} (Cédula: {user_to_delete.cedula})")
        
        # Elimina al usuario
        user_to_delete.delete()
        
        print(f"🗑️ El usuario ha sido eliminado exitosamente.")
        
    except CustomUser.DoesNotExist:
        # Se ejecuta si no se encuentra ningún usuario con esa cédula
        print(f"❌ Error: No se encontró ningún usuario con la cédula '{cedula}'.")
    except Exception as e:
        # Captura cualquier otro error inesperado
        print(f"🚨 Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    # Verifica que se haya proporcionado un argumento (la cédula)
    if len(sys.argv) != 2:
        print("Uso incorrecto. Debes proporcionar la cédula del usuario a eliminar.")
        print("Ejemplo: python delete_user.py 1234567890")
    else:
        # El segundo argumento (índice 1) es la cédula
        cedula_a_borrar = sys.argv[1]
        delete_user_by_cedula(cedula_a_borrar)