import mysql.connector

conn = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = conn.cursor()

word = input("Enter the word: ")
word = word.lower()

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    i = 1
    for result in results:
        print("Meaning " + str(i) + ": " + result[0])
        i += 1
else:
    print("No word found!")