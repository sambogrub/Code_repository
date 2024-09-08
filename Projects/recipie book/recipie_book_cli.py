#beginnings of the cli version

import sqlite3

class RecipeDatabase:
    def __init__(self, db_name = 'recipes.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        queries = [
            '''CREATE TABLE IF NOT EXISTS recipes(
            )'''
        ]