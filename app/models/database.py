from peewee import MySQLDatabase

database = MySQLDatabase(
    'product-fast',
    user='user',
    password='pas',
    host='local.fast-db',
    port=3306
)
