import sys
import requests
import psycopg2
from datetime import datetime
import json

HOST = "ec2-52-90-17-37.compute-1.amazonaws.com"
DATABASE = "revmax_dev"
USER = "dev_master"
PASSWORD = "master01"

HOST = "localhost"
DATABASE = "revmax_development"
USER = "nandukalidindi"
PASSWORD = "qwerty123"

AIRPORT_LIST = ['JFK', 'LGA', 'EWR']

FLIGHT_STATS_API = "https://api.flightstats.com/flex"
SCHEDULES = "schedules/rest/v1/json/to"

# jonathan@revmax.io
APP_ID = "83044e6f"
APP_KEY = "d69bf1d158ffe203fa0879108a8b2f71"

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

def persist_flight_arrivals_for_month(airport, year, month):
    print("FETCHING ARRIVALS AT FOR %s ON YEAR: %s AND MONTH: %s" % (airport, str(year), str(month)))
    for day in range(1, month_map()[month]+1):
        print("FETCHING ARRIVALS ON DAY " + str(day))
        persist_flight_arrivals_for_day(airport, year, month, day)

def persist_flight_arrivals_for_day(airport, year, month, day):
    for hour in range(0, 24):
        print("AT " + str(hour) + " HOUR")
        get_flight_arrivals(airport, year, month, day, hour)
        pg_connection.commit()


def get_flight_arrivals(airport, year, month, day, hour):
    full_response = requests.get(build_flight_stat_url_for_particular_hour(airport, year, month, day, hour)).json()
    if len(full_response.get('scheduledFlights')) > 0:
        for scheduled_flight_response in full_response.get('scheduledFlights'):
            if scheduled_flight_response['isCodeshare'] == False:
                scheduled_flight_response['flight_equipment_data'] = [x for x in full_response['appendix']['equipments'] if x['iata'] == scheduled_flight_response['flightEquipmentIataCode']][0]
                scheduled_flight_response['flight_type'] = scheduled_flight_response['flight_equipment_data']['name']
                scheduled_flight_response['flight_capacity'] = 10
                persist_flight_arrival(scheduled_flight_response)
    else:
        if full_response.get("error") and (full_response.get("error").get("httpStatusCode") == 403) and (full_response.get("error").get("errorCode") == "AUTH_FAILURE"):
            print("CRAWL WILL STOP NOW")
            print("MAKE SURE NEXT CRAWL STARTS FOR AIRPORT: %s, FROM YEAR: %s, MONTH: %s, DAY: %s, HOUR: %s" % (airport, year, month, day, hour))
            sys.exit("NO ARRIVAL SCHEDULES AVAILABLE")
        else:
            print("NO ARRIVALS FOR AIRPORT: %s, ON YEAR: %s, MONTH: %s, DAY: %s, HOUR: %s" % (airport, year, month, day, hour))

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
    cursor.execute(insert_sql, values)


def postgres_connection():
    try:
        connection = psycopg2.connect("dbname={} user={} host={} password={}".format(DATABASE, USER, HOST, PASSWORD))
    except:
        print("Unable to connect database. Please try again!")

    return connection;

pg_connection = postgres_connection()
cursor = pg_connection.cursor()

# for airport in AIRPORT_LIST:
#     persist_flight_arrivals_for_month(airport, 2017, 3)

persist_flight_arrivals_for_day('JFK', 2017, 3, 1)

pg_connection.commit()
pg_connection.close()
