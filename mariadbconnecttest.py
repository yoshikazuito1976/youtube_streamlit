#!/usr/bin/env python
import mariadb
name_host = '172.20.10.101'
host_port = 3306
name_user = 'mika'
user_pass = 'her_pa++++ssword'
name_base = 'foxglovetree'



try:
  conn = mariadb.connect(host = name_host, port = host_port,
             user = name_user, password = user_pass,
             database = name_base)
except mariadb.Error as e:
  print(f"Error connecting to MariaDB Platform: {e}")
  error = 60
  exit.exit(error)
cur = conn.cursor()

#ここにデータを入れるコードを書く。リスト型でも良いし、csvを展開しても良いし。
#うまくデータ入力できる方法がみつかったら、ローカルでの収集方法と整理方法を共有してもらえれば捗ると思います。


conn.commit()
conn.close()
