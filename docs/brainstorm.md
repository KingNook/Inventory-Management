# Brainstorm (04/07)

## Requirements

- Necessary
    - Each item has following fields filled out
        ~ Item ID (SQL ID / string)
        ~ Item Qty (int)
        ~ Batch Number (int) (check how batch processing / manufacturing works to find out if this is useful or if the fields need to be changed)
        ~ Quality Checked (bool)
        ~ Notes (?) (string ?)
    - Ability to add items
    - Accountability / version history
        ~ Ability to track who added & changed what items

- Useful
    - Importing data
        - data processing to clean and import data into the table (eg from misc format to csv, then csv directly to database)
    - Permissions
        - Database Administrator 
            ~ Access and editing permissions
        - User
            ~ Access for all columns
            ~ Editing for certain columns (eg qc might have editing only for 'quality checked' column)
    - Output data
        - ways to nicely display results of SQL queries

- Nice to Have
    - GUI
    - plot usage statistics
    - shortcuts / buttons to auto-search common queries eg
        ~ show all
        ~ deadline soon (eg 1 week)
        ~ all not Quality checked
        ~ all of certain batch number


## Platform

- Python
    - sql processing libraries
        ~ sqlite3 (SQLite)
            does not require extra requirements // comes with python 3
            `import sqlite3`
        ~ mysql (MySQL)
            requires Python SQL driver (`pip install mysql-connector-python`)
            `import mysql.connector` (?)
        ~ psycopg2 (PostgreSQL)
            requires Python SQL driver (`pip install psycopg2`)
            `import psycopg2`
    - can use Pandas for data analysis
        ~ User guide : https://pandas.pydata.org/docs/user_guide/index.html

- .NET
    - programming in C# 