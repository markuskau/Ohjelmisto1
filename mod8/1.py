import mysql.connector



connection = mysql.connector.connect(
         host="127.0.0.1",
         port= 3306,
         database="flight_game",
         user="root",
         password="lentopeli",
         autocommit=True
         )

def fetch_airport_by_icao(code):

    sql = (f"SELECT name, municipality "
           f"FROM airport WHERE ident='{code}'")

    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    print(result_row)
    return result_row


user_input = input("Anna lentokentän ICAO-koodi; ")
airport = fetch_airport_by_icao(user_input)


if airport:
    print(f"Haettu lentokenttä: {airport[0]}, {airport[1]}. ")

else:
    print("Lentokenttää ei löydetty annetulla koodilla. ")






