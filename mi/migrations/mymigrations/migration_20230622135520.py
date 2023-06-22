from django.db import connection
from mi.migrations.mymigrations.utils import has_table, create_table


def migration_20230622135520():
    exist = has_table('person')

    if not exist:
        ddl = """
            CREATE TABLE person (
                pe_id SERIAL PRIMARY KEY,
                pe_first_name VARCHAR(255),
                pe_last_name VARCHAR(255),
                pec_birth_date DATE
            );
        """

        create_table(ddl)
