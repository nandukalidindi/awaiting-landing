import requests
import psycopg2

HOST = "localhost"
DATABASE = "revmax_development"
USER = "nandukalidindi"
PASSWORD = "qwerty123"

pg_connection = postgres_connection()
cursor = pg_connection.cursor()

FLIGHT_STATS_API = "https://api.flightstats.com/flex" + "schedules/rest/v1/json/to/JFK/arriving/2017/12/30/0?appId=8146b8bf&appKey=c5a75fe109e3f3cb61a8789422d5b45e"
SCHEDULES = "schedules/rest/v1/json/to"
APP_ID = "8146b8bf"
APP_KEY = "c5a75fe109e3f3cb61a8789422d5b45e"

def build_flight_stat_url_for_particular_hour(airport, year, month, day, hour):
    return "%s/%s/%s/arriving/%s/%s/%s/%s?appId=%s&appKey=%s" % (FLIGHT_STATS_API, SCHEDULES, airport, year, month, day, hour, APP_ID, APP_KEY)


def get_flight_arrivals(airport, year, month, day, hour):
    arrival_response = requests.get(build_flight_stat_url_for_particular_hour(airport, year, month, day, hour))
    print(arrival_response)

get_flight_arrivals('JFK', 2017, 02, 10, 0)
