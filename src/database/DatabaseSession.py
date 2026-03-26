class DatabaseSession:
    from src.database import Database
    def __init__(self, db: 'Database'):
        self.db = db
        self.connection = None

    def __enter__(self):
        self.connection = self.db.connect()



    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            #sauvegarde(on dit a la base de donnee que tout est ok)
            self.connection.commit()

        else:
            #annuler l'operation(on dit a la base de donnee d'annuler l'execution de
            # la requete sql et de supprimer meme ce qui avait
            # deja reussit dans cette requete)
            self.connection.rollback()

        # on se deconnecte finalement de la base de donnee
        self.connection.close()
        return False

    # exc_type => type d'erreur lors del'execution d'une requete sql
    # exc_val => l'exception en lui meme
    # exc_tb => traceback (la pile d'appel)