"""
The script contains tools for handling LinguaPy project database
..//db_repo//linguapy.db
"""

import sqlite3
import os

conn = sqlite3.connect(f'{os.getcwd()}//db_repo//linguapy.db', check_same_thread = False)
cur = conn.cursor()

def add2db(table, columns, values):
    q_marks = str(tuple('?' for i in values)).replace("'", "")
    try:
        query = f"""
                INSERT INTO {table} {str(columns)} VALUES {q_marks}
                """
        cur.execute(query, values)
        conn.commit()
    except:
        raise Exception("The word is already in the dictionary!")

def get_allinfo_db(table):
    cur.execute(f"""SELECT * FROM {table}""")
    conn.commit()

    return cur.fetchall()

def get_columns_info_db(table, columns):
    columns = str(columns).replace("'", "").replace(")", "").replace("(", "")
    cur.execute(f"""SELECT {columns} FROM {table}""")
    conn.commit()

    return cur.fetchall()

def get_specific_words(table, columns, words):
    columns = str(columns).replace("'", "").replace(")", "").replace("(", "")
    cur.execute(f"""SELECT {columns} FROM {table}
                 WHERE word_eng in {words}
                 """)
    conn.commit()
    return cur.fetchall()

def get_specific_word(table, columns, word):
    columns = str(columns).replace("'", "").replace(")", "").replace("(", "")
    cur.execute(f"""SELECT {columns} FROM {table}
                 WHERE word_eng = "{word}"
                 """)
    conn.commit()
    return cur.fetchall()

def get_specific_word_rus(table, columns, word):
    columns = str(columns).replace("'", "").replace(")", "").replace("(", "")
    cur.execute(f"""SELECT {columns} FROM {table}
                 WHERE word_rus = "{word}"
                 """)
    conn.commit()
    return cur.fetchall()

def update_w_stat(word):
    cur.execute(f"""
                 UPDATE w_stat SET count_learned = count_learned + 1
                 WHERE word_eng = "{word}"
                 """)
    conn.commit()

def w_dict_getwords(words):
    cur.execute(f"""
                 SELECT * FROM w_dictionary
                 WHERE word_eng in {str(words)}
                 """)
    conn.commit()
    return cur.fetchall()
