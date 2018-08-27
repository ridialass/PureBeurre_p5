import records
from config import DB_NAME, DB_PASS, DB_USER


class Connexion:
    """ Connect or signup to the database. """

    def __init__(self):
        """ Init username password and name """
        self.db_username = DB_USER
        self.db_password = DB_PASS
        self.db_name = DB_NAME

    def connect_db(self):
        """ Connect to the database """
        self.db = records.Database('mysql://{}:{}@localhost'
                                   .format(self.db_username, self.db_password))
        self.db.query('USE {};'.format(self.db_name))


if __name__ == '__main__':
    app = Connexion()
    app.Connect_db()
