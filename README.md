Caerus Online Judge
===================

Copyright by Legend 2014.

A platform of online judge which is aimed at interview.

Set Environment
-------------------

System: Ubuntu-12.04LTS

> installed by many methods.

MySQL: MySQL-Server-5.5.38

> Install.

    $ apt-get install mysql-server mysql-client

> Configure.

    $ mysql -u root -p

> Create a database Caerus with UTF-8.

    mysql> CREATE DATABASE `Caerus` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

> Use username: caerus and password: caerusoj.

    mysql> GRANT ALL PRIVILEGES ON Caerus.* TO caerus@'localhost' identified by 'caerusoj';

> Verify it.

    $ mysql -u caerus -p caerusoj
    mysql> USE Caerus;
    mysql> SHOW TABLES;

Django: Django-1.6.5 on Python-2.7.3

> Install Python.

    $ apt-get install python

> Install SetupTools.

    $ apt-get install python-setuptools

> Install Django.

    $ easy_install Django

> Verify it.

    $ python -c "import django; print(django.get_version())"

> Install Python-MySQLdb.

    $ apt-get install python-mysqldb
