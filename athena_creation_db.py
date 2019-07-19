#!/usr/bin/env python

# Convert Db structure to Athena sql creation
# Usage: cat db_structure.txt | ./athena_creation_db database table > table.sql

import sys
import fileinput
database = sys.argv[1]
tableName = sys.argv[2]
index = 0
# columns = {}
columnCreating = ""
for line in sys.stdin.readlines():
    index += 1
    if index == 1: 
        continue
    arrs = line.split(',')
    columnName = arrs[0]
    columnType = arrs[1]
    if "varchar" in columnType:
        columnType = "string"
    elif "int" in columnType:
        columnType = "int"
    elif "date" in columnType:
        columnType = "date"
    elif "timestamp" in columnType:
        columnType = "date"
    columnCreating += "`{}` {},\n".format(columnName, columnType)
    # columns[columnName] = columnType
columnCreating = columnCreating[:-2]

# columnCreating = ""
# index=0
# for columnName, columnType in columns.items():
#     index += 1
#     columnCreating += "`{}` {}".format(columnName, columnType)
#     if index < len(columns):
#         columnCreating += ",\n"
# print columnCreating
f = open("./athena_sql_creation.txt", "r")
templateSqlCreation = f.read();
sqlCreation = templateSqlCreation.format(tableName, columnCreating, database, tableName)
sys.stdout.write(sqlCreation)