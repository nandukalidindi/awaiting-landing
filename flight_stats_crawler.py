import requests
import psycopg2
from datetime import datetime
import json

HOST = "localhost"
DATABASE = "revmax_development"
USER = "nandukalidindi"
PASSWORD = "qwerty123"

AIRPORT_LIST = ['JFK', 'LGA', 'EWR']

FLIGHT_STATS_API = "https://api.flightstats.com/flex"
SCHEDULES = "schedules/rest/v1/json/to"
APP_ID = "8146b8bf"
APP_KEY = "c5a75fe109e3f3cb61a8789422d5b45e"

# Yeah, yeah, we can use datetime delta method to see what the next date is,
# but why complicate things when a simple solution is lurking around
def month_map():
    return {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

def data_mapper():
    return {
        'carrierFsCode': 'carrier_fs_code',
        'flightNumber': 'flight_number',
        'departureAirportFsCode': 'departure_airport_fs_code',
        'arrivalAirportFsCode': 'arrival_airport_fs_code',
        'stops': 'stops',
        'departureTerminal': 'departure_terminal',
        'arrivalTerminal': 'arrival_terminal',
        'departureTime': 'departure_time',
        'arrivalTime': 'arrival_time',
        'flightEquipmentIataCode': 'flight_equipment_iata_code',
        'serviceType': 'service_type',
        'serviceClasses': 'service_classes',
        'trafficRestrictions': 'traffic_restrictions',
    }


def build_flight_stat_url_for_particular_hour(airport, year, month, day, hour):
    return "%s/%s/%s/arriving/%s/%s/%s/%s?appId=%s&appKey=%s" % (FLIGHT_STATS_API, SCHEDULES, airport, year, month, day, hour, APP_ID, APP_KEY)

def persist_flight_arrivals_for_a_month(airport, year, month):
    for day in range(0, month_map()[month]):
        persist_flight_arrivals_for_a_day(airport, year, month, day)

def persist_flight_arrivals_for_a_day(airport, year, month, day):
    for hour in range(0, 24):
        get_flight_arrivals(airport, year, month, day, hour)


def get_flight_arrivals(airport, year, month, day, hour):
    full_response = requests.get(build_flight_stat_url_for_particular_hour(airport, year, month, day, hour)).json()
    for scheduled_flight_response in full_response.get('scheduledFlights'):
        scheduled_flight_response['flight_equipment_data'] = [x for x in full_response['appendix']['equipments'] if x['iata'] == scheduled_flight_response['flightEquipmentIataCode']][0]
        scheduled_flight_response['flight_type'] = scheduled_flight_response['flight_equipment_data']['name']
        scheduled_flight_response['flight_capacity'] = 10
        persist_flight_arrival(scheduled_flight_response)

def prepare_SQL_statement(response):
    schema = data_mapper()
    columns = []
    values = []
    for k, v in response.items():
        if(schema.get(k) != None):
            columns.append(schema.get(k))
            values.append(response.get(k))

    columns.append('flight_equipment_data')
    values.append(json.dumps(response.get('flight_equipment_data')))

    columns.append('flight_type')
    values.append(response.get('flight_type'))

    columns.append('flight_capacity')
    values.append(response.get('flight_capacity'))

    columns.append('type')
    values.append('flight_arrivals')

    columns.append('complete_response')
    values.append(json.dumps(response))

    columns.append('created_at')
    values.append(str(datetime.now().replace(microsecond=0).isoformat()))

    columns.append('updated_at')
    values.append(str(datetime.now().replace(microsecond=0).isoformat()))

    return ",".join(columns), values

def persist_flight_arrival(response):
    formatter_list = []
    sql_tuple = prepare_SQL_statement(response)
    for i in range(0, len(sql_tuple[1])):
        formatter_list.append('%s')

    formatter_list = ",".join(formatter_list)
    insert_sql = "INSERT INTO revmax_flight_arrival (" + sql_tuple[0] + ") VALUES (" + formatter_list + ")"
    values = sql_tuple[1]
    print("INSERT SQL IS " + insert_sql)
    print("VALUES ARE" + str(values))
    cursor.execute(insert_sql, values)


def postgres_connection():
    try:
        connection = psycopg2.connect("dbname={} user={} host={} password={}".format(DATABASE, USER, HOST, PASSWORD))
    except:
        print("Unable to connect database. Please try again!")

    return connection;

pg_connection = postgres_connection()
cursor = pg_connection.cursor()

# print(response)
persist_flight_arrivals_for_a_day('JFK', 2017, 2, 14)
pg_connection.commit()
pg_connection.close()
