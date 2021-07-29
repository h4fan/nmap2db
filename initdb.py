#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

db_str = 'nmapscanresult.db'

conn = sqlite3.connect(db_str)

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE records
             (host text, ip text, port text,state text, protocol text, service text,version text, scandate text)''')



# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
