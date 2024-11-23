def reproducir_contenido(contenido_id):
    """Reproducir contenido en alta calidad"""
    db = SessionLocal()
    try:
        contenido = CRUD_contenidos.reproducir_contenido(db, contenido_id)
        if contenido:
            return jsonify({'url_reproduccion': contenido.url_video})
        else:
            return jsonify({'mensaje': 'Contenido no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()