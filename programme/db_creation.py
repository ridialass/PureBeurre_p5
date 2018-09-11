#! /usr/bin/env python3
# coding: utf-8
"""BD_creation module connects to server, creates the db and feed it."""

import records
from db_populate_tables import DatabaseFeeder
from config import DB_NAME, DB_PASS, DB_USER


class DatabaseCreator:
    """Database class creator."""

    def __init__(self):
        """Initiate username , password , name of the database and connect."""
        self.db_name = DB_NAME
        self.db_username = DB_USER
        self.db_password = DB_PASS
        self.db = records.Database('mysql+mysqlconnector://{}:{}@localhost:6606/?charset=utf8mb4'
                                   .format(self.db_username, self.db_password))

    def create_database(self):
        """Create database."""
        self.db.query("DROP DATABASE IF EXISTS {};".format(self.db_name))
        self.db.query("CREATE DATABASE {} CHARACTER SET 'utf8mb4'"
                      .format(self.db_name))
        self.db.query("USE {};".format(self.db_name))

    def create_product_table(self):
        """Create a table listing the products of the database."""
        self.db.query("""CREATE TABLE product (
            code BIGINT(20) UNSIGNED NOT NULL PRIMARY KEY,
            product_name VARCHAR(255) NOT NULL,
            brand VARCHAR(255) NOT NULL,
            url_link VARCHAR(255) NOT NULL,
            nutrition_grade_fr CHAR(1) NOT NULL
            )""")

    def create_category_table(self):
        """Create a table linking a product to categories."""
        self.db.query("""CREATE TABLE category (
            id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL UNIQUE
            )""")

    def create_store_table(self):
        """Create a table linking a product to stores."""
        self.db.query("""CREATE TABLE store (
            id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL UNIQUE
            )""")

    def create_product_category_table(self):
        """Create a table joining the products at their related categories."""
        self.db.query("""CREATE TABLE product_category (
            id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
            product_code BIGINT UNSIGNED REFERENCES product(code),
            category_id MEDIUMINT UNSIGNED REFERENCES category(id)
            )""")

    def create_product_store_table(self):
        """Create a table joining the different products at related stores."""
        self.db.query("""CREATE TABLE product_store (
            id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
            product_code BIGINT UNSIGNED REFERENCES product(code),
            store_id MEDIUMINT UNSIGNED REFERENCES store(id)
            )""")

    def create_favorite_table(self):
        """Create a table where to save results as 'favorites' if needed."""
        self.db.query("""CREATE TABLE favorite (
            id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
            product_id BIGINT UNSIGNED REFERENCES product(code),
            substitute_id BIGINT UNSIGNED REFERENCES product(code)
            )""")

    def create_tables(self):
        """Launch the different table creators of the database."""
        self.create_product_table()
        self.create_category_table()
        self.create_store_table()
        self.create_product_category_table()
        self.create_product_store_table()
        self.create_favorite_table()

    def add_contents_to_db(self):
        """Add data to the db using DbManagement class."""
        feeder = DatabaseFeeder()
        feeder.fetch_data()
        feeder.clean_tables()
        feeder.feed_products()


def main():
    """Entry point of the module."""
    print("Database creation started, please wait...")
    db_script = DatabaseCreator()
    db_script.create_database()
    db_script.create_tables()
    print("Creation completed.")
    print("Database feeding started, please wait...")
    db_script.add_contents_to_db()
    print("Feeding completed.")

if __name__ == '__main__':
    main()
