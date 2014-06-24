"""
This is a specific trivial example using DE's user-defined type acknowledgment_state.
To run in bash: python example.py
"""
import psycopg2

from db.userdefined import get_type_oid, get_type_name


def main():
    conn = psycopg2.connect("host=host dbname=dbname "
                            "user=user password=password")
    a_state_oid = get_type_oid(conn.cursor(), "acknowledgment_state", "public")
    a_state_name = get_type_oid(conn.cursor(), a_state_oid, "public")
    print "%s = %s" % (a_state_name, a_state_oid)


if __name__ == "__main__":
    main()
