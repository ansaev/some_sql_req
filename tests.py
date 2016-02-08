# -*- coding: utf-8 -*-
import sys
from req import sql_request
import sqlite3
reload(sys)
sys.setdefaultencoding('utf-8')


def test_request():
    conn = sqlite3.connect('test.db')
    rez = conn.execute(sql_request).fetchall()
    conn.close()
    assert rez == [("Лера Страза", 0), ("Платон Щукин", 2), ("Георгий Атласов", 2)]