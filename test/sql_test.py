
import os
import re
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model.sqlutils import SqlUtils
sql = SqlUtils()
sql.create_connection()
print(sql.get_accounts_list())