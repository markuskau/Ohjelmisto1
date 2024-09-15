import mysql.connector



connection = mysql.connector.connect(
         host="127.0.0.1",
         port= 3306,
         database="flight_game",
         user="root",
         password="lentopeli",
         autocommit=True
         )

def fetch_airport_code_by_airport_count(code):
    sql = (f" SELECT airport.type, count(*) AS airport_count "
           f" FROM airport"
           f" INNER JOIN country ON airport.iso_country = country.iso_country" 
           f" WHERE country.iso_country = '{code}'"
           f" GROUP BY airport.type")

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result






country_code = input("Anna maakoodi: ")
country = fetch_airport_code_by_airport_count(country_code)

if country:
    print(f"Tulokset maakoodilla: {country_code}.")
    for row in country:
        print(f"Airport Type: {row[0]}, Count: {row[1]}")

else:
    print("Maakoodilla ei tuloksia.")





