import sqlite3

conn = sqlite3.connect('crudapplication.db')

c = conn.cursor()

c.execute("""CREATE TABLE emp(empid integer primary key AUTOINCREMENT, name text not null, email text, phone text, address text, joining_date text,  total_projects text, total_test_case text )""")
c.execute("""CREATE TABLE empe(empid integer primary key AUTOINCREMENT, name text not null, email text, phone text, address text, joining_date text,  total_projects text, total_test_case text )""")

c.execute("""CREATE TABLE emp_d(empid integer primary key AUTOINCREMENT, name text not null, email text, phone text, address text, joining_date text,  total_projects text, total_test_case text )""")

c.execute("""CREATE TABLE emp_e(empid integer primary key AUTOINCREMENT, name text not null, email text, phone text, address text, joining_date text,  total_projects text, total_test_case text )""")

c.execute("""CREATE TABLE emp_i(empid integer primary key AUTOINCREMENT, name text not null, email text, phone text, address text, joining_date text,  total_projects text, total_test_case text )""")

c.execute("""CREATE TABLE emp_k(empid integer primary key AUTOINCREMENT, name text not null, email text, phone text, address text, joining_date text,  total_projects text, total_test_case text )""")

c.execute("""CREATE TABLE emp_g(empid integer primary key AUTOINCREMENT, name text not null, email text, phone text, address text, joining_date text,  total_projects text, total_test_case text )""")

c.execute("""CREATE TABLE emp_n(empid integer primary key AUTOINCREMENT, name text not null, email text, phone text, address text, joining_date text,  total_projects text, total_test_case text )""")

c.execute("""CREATE TABLE emp_m(empid integer primary key AUTOINCREMENT, name text not null, email text, phone text, address text, joining_date text,  total_projects text, total_test_case text )""")

c.execute("""CREATE TABLE emp_y(empid integer primary key AUTOINCREMENT, name text not null, email text, phone text, address text, joining_date text,  total_projects text, total_test_case text )""")

c.execute("""CREATE TABLE emp_o(empid integer primary key AUTOINCREMENT, name text not null, email text, phone text, address text, joining_date text,  total_projects text, total_test_case text )""")

c.execute("""CREATE TABLE empe_o(empid integer primary key AUTOINCREMENT, name text not null, email text, phone text, address text, joining_date text,  total_projects text, total_test_case text )""")

c.execute("""CREATE TABLE empe_k(empid integer primary key AUTOINCREMENT, name text not null, email text, phone text, address text, joining_date text,  total_projects text, total_test_case text )""")

c.execute("""CREATE TABLE empe_m(empid integer primary key AUTOINCREMENT, name text not null, email text, phone text, address text, joining_date text,  total_projects text, total_test_case text )""")

c.execute("""CREATE TABLE empe_n(empid integer primary key AUTOINCREMENT, name text not null, email text, phone text, address text, joining_date text,  total_projects text, total_test_case text )""")

c.execute("""CREATE TABLE emp_a(empid integer primary key AUTOINCREMENT, name text not null, email text, phone text, address text, joining_date text,  total_projects text, total_test_case text )""")






conn.commit()
conn.close()

