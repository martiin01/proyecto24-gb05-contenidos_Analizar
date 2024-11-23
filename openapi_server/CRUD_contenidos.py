from sqlalchemy.orm import Session
from sqlalchemy import desc
from openapi_server.databaseContenido import Contenido as ContenidoDB

def obtener_contenido_por_id(db: Session, contenido_id: int):
    try:
        contenido = db.query(ContenidoDB).filter(ContenidoDB.id_contenido == contenido_id).first()
        if contenido:
            return contenido
        else:
            return None
    except Exception as e:
        raise e