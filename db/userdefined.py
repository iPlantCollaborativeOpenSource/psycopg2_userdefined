"""
User defined type utilities for psycopg2.
"""
import psycopg2


def get_type_oid(cursor, typename, namespace="public"):
    """
    Get a user defined type oid using a psycopg2 curson, the typename
    and namespace.
    """
    cursor.execute("""
              SELECT pgt.oid FROM pg_type pgt
              JOIN pg_namespace pgn ON pgt.typnamespace = pgn.oid
              WHERE pgt.typname = %(typename)s
              AND   pgn.nspname = %(namespace)s;""",
                   {'typename': typename,
                    'namespace': namespace})
    return cursor.fetchone()[0]
