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