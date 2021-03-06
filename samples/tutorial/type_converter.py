#------------------------------------------------------------------------------
# type_converter.py (Section 6.2)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Copyright (c) 2017, 2021, Oracle and/or its affiliates. All rights reserved.
#------------------------------------------------------------------------------

import cx_Oracle
import db_config

con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
cur = con.cursor()

for value, in cur.execute("select 0.1 from dual"):
    print("Value:", value, "* 3 =", value * 3)
