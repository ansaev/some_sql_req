import sys
# -*- coding: utf-8 -*-
from req import sql_request
import sqlite3


def test_request():
    conn = sqlite3.connect('test.db')
    rez = conn.execute(sql_request).fetchall()
    # rez = conn.fetchall()
    print(rez)
    conn.close()
    assert rez == [("Платон Щукин", 2), ("Георгий Атласов", 1)]