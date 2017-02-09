import requests
import psycopg2

HOST = "localhost"
DATABASE = "revmax_development"
USER = "nandukalidindi"
PASSWORD = "qwerty123"

FLIGHT_STATS_API = "https://api.flightstats.com/flex"
SCHEDULES = "schedules/rest/v1/json/to"
APP_ID = "8146b8bf"
APP_KEY = "c5a75fe109e3f3cb61a8789422d5b45e"

def build_flight_stat_url_for_particular_hour(airport, year, month, day, hour):
    return "%s/%s/%s/arriving/%s/%s/%s/%s?appId=%s&appKey=%s" % (FLIGHT_STATS_API, SCHEDULES, airport, year, month, day, hour, APP_ID, APP_KEY)


def get_flight_arrivals(airport, year, month, day, hour):
    arrival_response = requests.get(build_flight_stat_url_for_particular_hour(airport, year, month, day, hour))
    print(arrival_response.json())

get_flight_arrivals('JFK', 2017, 2, 10, 0)

# def postgres_connection():
#     try:
#         connection = psycopg2.connect("dbname={} user={} host={} password={}".format(DATABASE, USER, HOST, PASSWORD))
#     except:
#         print("Unable to connect database. Please try again!")
#
#     return connection;
#
# pg_connection = postgres_connection()
# cursor = pg_connection.cursor()
