try:
    from src.logger import logging
    from src.exception import ExcepcionPersonalizada
    import sys
    print("✅ Éxito: Todas las importaciones de 'src' funcionan correctamente.")
except ImportError as e:
    print(f"❌ Error: No se encuentra el módulo. Detalle: {e}")
except Exception as e:
    print(f"⚠️ Ocurrió otro error: {e}")


