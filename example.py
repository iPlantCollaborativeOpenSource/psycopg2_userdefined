"""
This is a specific example using DE's user-defined type acknowledgment_state.
To run in bash: python example.py
"""
import psycopg2

from db.userdefined import get_type_oid


def main():
    conn = psycopg2.connect("host=host dbname=dbname "
                            "user=user password=password")
    a_state_oid = get_type_oid(conn.cursor(), "acknowledgment_state", "public")
    print a_state_oid


if __name__ == "__main__":
    main()
