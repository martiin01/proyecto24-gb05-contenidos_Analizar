import connexion
from flask import jsonify
from openapi_server.database_logica import SessionLocal
from openapi_server import CRUD_contenidos

def contenidos_id_get(contenido_id):
    """Obtener detalles de un contenido específico por su ID"""
    db = SessionLocal()
    try:
        contenido = CRUD_contenidos.obtener_contenido_por_id(db, contenido_id)
        if contenido:
            return jsonify(contenido.to_dict())
        else:
            return jsonify({'mensaje': 'Contenido no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()
def obtener_catalogo(genero=None, orden=None):
    """Obtener catálogo completo de contenidos"""
    db = SessionLocal()
    try:
        contenidos_list = CRUD_contenidos.obtener_catalogo(db, genero, orden)
        return jsonify(contenidos_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()