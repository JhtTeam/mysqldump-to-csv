#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Convert ShiftJIS to UTF-8
# Usage: cat ShiftJIS.txt | ./convert.py > UTF8.txt
# Alternative method: cat ShiftJIS.txt | iconv -f shift_jis -t utf8 > UTF8.txt

import sys
import fileinput
tableName = sys.argv[1]
index = 0
columns = {}
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
    columns[columnName] = columnType

columnCreating = ""
index=0
for columnName, columnType in columns.items():
    index += 1
    columnCreating += "`{}` {}".format(columnName, columnType)
    if index < len(columns):
        columnCreating += ",\n"

f = open("./athena_sql_creation.txt", "r")
templateSqlCreation = f.read();
sqlCreation = templateSqlCreation.format(tableName, columnCreating, tableName)
sys.stdout.write(sqlCreation)
# f = open("./{}.sql".format(tableName), "w+")
# f.write(sqlCreation)