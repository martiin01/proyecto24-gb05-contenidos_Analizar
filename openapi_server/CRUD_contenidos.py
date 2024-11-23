def obtener_catalogo(db: Session, genero: str = None, orden: str = None):
    try:
        query = db.query(ContenidoDB)
        if genero:
            query = query.filter(ContenidoDB.genero.ilike(f'%{genero}%'))
        if orden:
            if orden.lower() == 'popularidad':
                query = query.order_by(desc(ContenidoDB.rating))
            elif orden.lower() == 'fecha':
                query = query.order_by(desc(ContenidoDB.año_lanzamiento))
        contenidos_db = query.all()
        contenidos_list = [contenido.to_dict() for contenido in contenidos_db]
        return contenidos_list
    except Exception as e:
        raise e