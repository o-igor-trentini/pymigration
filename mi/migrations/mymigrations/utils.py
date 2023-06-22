from django.db import connection
from string import Template


def has_table(table_name):
    with connection.cursor() as cursor:
        try:
            query = "SELECT EXISTS (SELECT 1 FROM pg_tables WHERE tablename = %s);"
            cursor.execute(query, [table_name])

            return cursor.fetchone()[0]

        except Exception as e:
            return "Não foi possível verificar se a tabela existe [erro: " + str(e) + "]"


def create_table(ddl):
    with connection.cursor() as cursor:
        try:
            cursor.execute(ddl)

        except Exception as e:
            return "Não foi possível criar a tabela [erro: " + str(e) + "]"
