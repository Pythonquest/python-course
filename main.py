import sqlite3

conn = sqlite3.connect('tutorial.db')

c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)')


def enter_dynamic_data(lang, ver, sk):
    c.execute("INSERT INTO example (Language, Version, Skill) VALUES(?, ?, ?)", (lang, str(ver), sk))
    conn.commit()


def read_from_database(sql):
    #sql = "SELECT * FROM example WHERE Skill = 'Beginner'"
    try:
        if sql.upper() != 'EXIT':
            for row in c.execute(sql):
                print(row)
    except Exception as e:
        print(e)


def main():
    sql_query = ''
    while (sql_query.upper()) != 'EXIT':
        sql_query = input('Type in your desired SQL (or "EXIT" to quit): ')
        read_from_database(sql_query)


main()
#read_from_database()
#enter_dynamic_data('Python', 10.0, 'Expert')


conn.close()
