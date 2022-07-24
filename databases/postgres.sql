postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 test      | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =Tc/postgres         +
           |          |          |             |             | postgres=CTc/postgres+
           |          |          |             |             | viett=CTc/postgres
(4 rows)

postgres=# CREATE DATABASE sqltutorial;
CREATE DATABASE
postgres=# GRANT ALL PRIVILEGES ON DATABASE sqltutorial TO viett;
GRANT
postgres=# \l
                                   List of databases
    Name     |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-------------+----------+----------+-------------+-------------+-----------------------
 postgres    | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 sqltutorial | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =Tc/postgres         +
             |          |          |             |             | postgres=CTc/postgres+
             |          |          |             |             | viett=CTc/postgres
 template0   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
             |          |          |             |             | postgres=CTc/postgres
 template1   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
             |          |          |             |             | postgres=CTc/postgres
 test        | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =Tc/postgres         +
             |          |          |             |             | postgres=CTc/postgres+
             |          |          |             |             | viett=CTc/postgres
(5 rows)

-- run $VENV/bin/initialize_tutorial_db development.ini here
postgres=# \c sqltutorial 
You are now connected to database "sqltutorial" as user "postgres".
sqltutorial=# \c sqltutorial 
You are now connected to database "sqltutorial" as user "postgres".
sqltutorial=# \dt
         List of relations
 Schema |   Name    | Type  | Owner 
--------+-----------+-------+-------
 public | wikipages | table | viett
(1 row)

sqltutorial=# 
