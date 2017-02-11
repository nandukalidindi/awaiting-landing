import requests
import psycopg2
from datetime import datetime
import json

full_response = {
 "request": {
  "airport": {
   "requestedCode": "JFK",
   "fsCode": "JFK"
  },
  "codeType": {},
  "departing": False,
  "date": {
   "year": "2017",
   "month": "2",
   "day": "10",
   "interpreted": "2017-02-10"
  },
  "hourOfDay": {
   "requested": "0",
   "interpreted": 0
  },
  "url": "https://api.flightstats.com/flex/schedules/rest/v1/json/to/JFK/arriving/2017/02/10/0"
 },
 "scheduledFlights": [
  {
   "carrierFsCode": "DL",
   "flightNumber": "2040",
   "departureAirportFsCode": "SFO",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "departureTerminal": "1",
   "arrivalTerminal": "4",
   "departureTime": "2017-02-09T16:00:00.000",
   "arrivalTime": "2017-02-10T00:32:00.000",
   "flightEquipmentIataCode": "75W",
   "isCodeshare": False,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "J",
    "Y"
   ],
   "trafficRestrictions": [],
   "codeshares": [
    {
     "carrierFsCode": "AZ",
     "flightNumber": "3435",
     "serviceType": "J",
     "serviceClasses": [
      "J",
      "Y"
     ],
     "trafficRestrictions": [
      "G"
     ],
     "referenceCode": 11554327
    },
    {
     "carrierFsCode": "VS",
     "flightNumber": "4856",
     "serviceType": "J",
     "serviceClasses": [
      "R",
      "J",
      "Y"
     ],
     "trafficRestrictions": [
      "Q"
     ],
     "referenceCode": 11554328
    }
   ],
   "referenceCode": "29-3463914--"
  },
  {
   "carrierFsCode": "AZ",
   "flightNumber": "3435",
   "departureAirportFsCode": "SFO",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "departureTerminal": "1",
   "arrivalTerminal": "4",
   "departureTime": "2017-02-09T16:00:00.000",
   "arrivalTime": "2017-02-10T00:32:00.000",
   "flightEquipmentIataCode": "75W",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "J",
    "Y"
   ],
   "trafficRestrictions": [
    "G"
   ],
   "operator": {
    "carrierFsCode": "DL",
    "flightNumber": "2040",
    "serviceType": "J",
    "serviceClasses": [
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-3463914--11554327"
  },
  {
   "carrierFsCode": "VS",
   "flightNumber": "4856",
   "departureAirportFsCode": "SFO",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "departureTerminal": "1",
   "arrivalTerminal": "4",
   "departureTime": "2017-02-09T16:00:00.000",
   "arrivalTime": "2017-02-10T00:32:00.000",
   "flightEquipmentIataCode": "75W",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "R",
    "J",
    "Y"
   ],
   "trafficRestrictions": [
    "Q"
   ],
   "operator": {
    "carrierFsCode": "DL",
    "flightNumber": "2040",
    "serviceType": "J",
    "serviceClasses": [
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-3463914--11554328"
  },
  {
   "carrierFsCode": "B6",
   "flightNumber": "690",
   "departureAirportFsCode": "MCO",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "5",
   "departureTime": "2017-02-09T21:48:00.000",
   "arrivalTime": "2017-02-10T00:09:00.000",
   "flightEquipmentIataCode": "321",
   "isCodeshare": False,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "R",
    "F",
    "J",
    "Y"
   ],
   "trafficRestrictions": [],
   "codeshares": [
    {
     "carrierFsCode": "HA",
     "flightNumber": "2067",
     "serviceType": "J",
     "serviceClasses": [
      "J",
      "Y"
     ],
     "trafficRestrictions": [
      "X"
     ],
     "referenceCode": 2419850
    },
    {
     "carrierFsCode": "SA",
     "flightNumber": "7365",
     "serviceType": "J",
     "serviceClasses": [
      "Y"
     ],
     "trafficRestrictions": [
      "G"
     ],
     "referenceCode": 11080447
    },
    {
     "carrierFsCode": "EK",
     "flightNumber": "6748",
     "serviceType": "J",
     "serviceClasses": [
      "R",
      "Y"
     ],
     "trafficRestrictions": [
      "Y"
     ],
     "referenceCode": 11080448
    }
   ],
   "referenceCode": "29-2419370--"
  },
  {
   "carrierFsCode": "SA",
   "flightNumber": "7365",
   "departureAirportFsCode": "MCO",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "5",
   "departureTime": "2017-02-09T21:48:00.000",
   "arrivalTime": "2017-02-10T00:09:00.000",
   "flightEquipmentIataCode": "321",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "Y"
   ],
   "trafficRestrictions": [
    "G"
   ],
   "operator": {
    "carrierFsCode": "B6",
    "flightNumber": "690",
    "serviceType": "J",
    "serviceClasses": [
     "R",
     "F",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-2419370--11080447"
  },
  {
   "carrierFsCode": "EK",
   "flightNumber": "6748",
   "departureAirportFsCode": "MCO",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "5",
   "departureTime": "2017-02-09T21:48:00.000",
   "arrivalTime": "2017-02-10T00:09:00.000",
   "flightEquipmentIataCode": "321",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "R",
    "Y"
   ],
   "trafficRestrictions": [
    "Y"
   ],
   "operator": {
    "carrierFsCode": "B6",
    "flightNumber": "690",
    "serviceType": "J",
    "serviceClasses": [
     "R",
     "F",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-2419370--11080448"
  },
  {
   "carrierFsCode": "Y4",
   "flightNumber": "894",
   "departureAirportFsCode": "GDL",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "departureTerminal": "1",
   "departureTime": "2017-02-09T18:34:00.000",
   "arrivalTime": "2017-02-10T00:20:00.000",
   "flightEquipmentIataCode": "320",
   "isCodeshare": False,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "Y"
   ],
   "trafficRestrictions": [],
   "codeshares": [],
   "referenceCode": "29-1461262--"
  },
  {
   "carrierFsCode": "B6",
   "flightNumber": "1024",
   "departureAirportFsCode": "LAX",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "departureTerminal": "3",
   "arrivalTerminal": "5",
   "departureTime": "2017-02-09T16:40:00.000",
   "arrivalTime": "2017-02-10T00:49:00.000",
   "flightEquipmentIataCode": "32S",
   "isCodeshare": False,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "R",
    "F",
    "J",
    "Y"
   ],
   "trafficRestrictions": [],
   "codeshares": [],
   "referenceCode": "29-2036269--"
  },
  {
   "carrierFsCode": "B6",
   "flightNumber": "26",
   "departureAirportFsCode": "TPA",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "5",
   "departureTime": "2017-02-09T21:36:00.000",
   "arrivalTime": "2017-02-10T00:09:00.000",
   "flightEquipmentIataCode": "321",
   "isCodeshare": False,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "R",
    "F",
    "J",
    "Y"
   ],
   "trafficRestrictions": [],
   "codeshares": [
    {
     "carrierFsCode": "HA",
     "flightNumber": "2073",
     "serviceType": "J",
     "serviceClasses": [
      "J",
      "Y"
     ],
     "trafficRestrictions": [
      "X"
     ],
     "referenceCode": 11696984
    },
    {
     "carrierFsCode": "SA",
     "flightNumber": "7385",
     "serviceType": "J",
     "serviceClasses": [
      "Y"
     ],
     "trafficRestrictions": [
      "G"
     ],
     "referenceCode": 11696985
    },
    {
     "carrierFsCode": "EK",
     "flightNumber": "6768",
     "serviceType": "J",
     "serviceClasses": [
      "R",
      "Y"
     ],
     "trafficRestrictions": [
      "Y"
     ],
     "referenceCode": 11696986
    },
    {
     "carrierFsCode": "QR",
     "flightNumber": "4162",
     "serviceType": "J",
     "serviceClasses": [
      "Y"
     ],
     "trafficRestrictions": [
      "Y"
     ],
     "referenceCode": 11696987
    }
   ],
   "referenceCode": "29-3787268--"
  },
  {
   "carrierFsCode": "HA",
   "flightNumber": "2073",
   "departureAirportFsCode": "TPA",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "5",
   "departureTime": "2017-02-09T21:36:00.000",
   "arrivalTime": "2017-02-10T00:09:00.000",
   "flightEquipmentIataCode": "321",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "J",
    "Y"
   ],
   "trafficRestrictions": [
    "X"
   ],
   "operator": {
    "carrierFsCode": "B6",
    "flightNumber": "26",
    "serviceType": "J",
    "serviceClasses": [
     "R",
     "F",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-3787268--11696984"
  },
  {
   "carrierFsCode": "SA",
   "flightNumber": "7385",
   "departureAirportFsCode": "TPA",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "5",
   "departureTime": "2017-02-09T21:36:00.000",
   "arrivalTime": "2017-02-10T00:09:00.000",
   "flightEquipmentIataCode": "321",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "Y"
   ],
   "trafficRestrictions": [
    "G"
   ],
   "operator": {
    "carrierFsCode": "B6",
    "flightNumber": "26",
    "serviceType": "J",
    "serviceClasses": [
     "R",
     "F",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-3787268--11696985"
  },
  {
   "carrierFsCode": "EK",
   "flightNumber": "6768",
   "departureAirportFsCode": "TPA",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "5",
   "departureTime": "2017-02-09T21:36:00.000",
   "arrivalTime": "2017-02-10T00:09:00.000",
   "flightEquipmentIataCode": "321",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "R",
    "Y"
   ],
   "trafficRestrictions": [
    "Y"
   ],
   "operator": {
    "carrierFsCode": "B6",
    "flightNumber": "26",
    "serviceType": "J",
    "serviceClasses": [
     "R",
     "F",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-3787268--11696986"
  },
  {
   "carrierFsCode": "QR",
   "flightNumber": "4162",
   "departureAirportFsCode": "TPA",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "5",
   "departureTime": "2017-02-09T21:36:00.000",
   "arrivalTime": "2017-02-10T00:09:00.000",
   "flightEquipmentIataCode": "321",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "Y"
   ],
   "trafficRestrictions": [
    "Y"
   ],
   "operator": {
    "carrierFsCode": "B6",
    "flightNumber": "26",
    "serviceType": "J",
    "serviceClasses": [
     "R",
     "F",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-3787268--11696987"
  },
  {
   "carrierFsCode": "DL",
   "flightNumber": "2362",
   "departureAirportFsCode": "LAX",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "departureTerminal": "5",
   "arrivalTerminal": "4",
   "departureTime": "2017-02-09T16:05:00.000",
   "arrivalTime": "2017-02-10T00:25:00.000",
   "flightEquipmentIataCode": "75W",
   "isCodeshare": False,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "J",
    "Y"
   ],
   "trafficRestrictions": [],
   "codeshares": [
    {
     "carrierFsCode": "KE",
     "flightNumber": "7537",
     "serviceType": "J",
     "serviceClasses": [
      "Y"
     ],
     "trafficRestrictions": [
      "Q"
     ],
     "referenceCode": 10883061
    },
    {
     "carrierFsCode": "VA",
     "flightNumber": "6645",
     "serviceType": "J",
     "serviceClasses": [
      "J",
      "Y"
     ],
     "trafficRestrictions": [
      "X"
     ],
     "referenceCode": 10883062
    },
    {
     "carrierFsCode": "VS",
     "flightNumber": "4748",
     "serviceType": "J",
     "serviceClasses": [
      "R",
      "J",
      "Y"
     ],
     "trafficRestrictions": [
      "Q"
     ],
     "referenceCode": 10883063
    }
   ],
   "referenceCode": "29-2036740--"
  },
  {
   "carrierFsCode": "KE",
   "flightNumber": "7537",
   "departureAirportFsCode": "LAX",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "departureTerminal": "5",
   "arrivalTerminal": "4",
   "departureTime": "2017-02-09T16:05:00.000",
   "arrivalTime": "2017-02-10T00:25:00.000",
   "flightEquipmentIataCode": "75W",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "Y"
   ],
   "trafficRestrictions": [
    "Q"
   ],
   "operator": {
    "carrierFsCode": "DL",
    "flightNumber": "2362",
    "serviceType": "J",
    "serviceClasses": [
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-2036740--10883061"
  },
  {
   "carrierFsCode": "VA",
   "flightNumber": "6645",
   "departureAirportFsCode": "LAX",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "departureTerminal": "5",
   "arrivalTerminal": "4",
   "departureTime": "2017-02-09T16:05:00.000",
   "arrivalTime": "2017-02-10T00:25:00.000",
   "flightEquipmentIataCode": "75W",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "J",
    "Y"
   ],
   "trafficRestrictions": [
    "X"
   ],
   "operator": {
    "carrierFsCode": "DL",
    "flightNumber": "2362",
    "serviceType": "J",
    "serviceClasses": [
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-2036740--10883062"
  },
  {
   "carrierFsCode": "VS",
   "flightNumber": "4748",
   "departureAirportFsCode": "LAX",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "departureTerminal": "5",
   "arrivalTerminal": "4",
   "departureTime": "2017-02-09T16:05:00.000",
   "arrivalTime": "2017-02-10T00:25:00.000",
   "flightEquipmentIataCode": "75W",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "R",
    "J",
    "Y"
   ],
   "trafficRestrictions": [
    "Q"
   ],
   "operator": {
    "carrierFsCode": "DL",
    "flightNumber": "2362",
    "serviceType": "J",
    "serviceClasses": [
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-2036740--10883063"
  },
  {
   "carrierFsCode": "HA",
   "flightNumber": "2067",
   "departureAirportFsCode": "MCO",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "5",
   "departureTime": "2017-02-09T21:48:00.000",
   "arrivalTime": "2017-02-10T00:09:00.000",
   "flightEquipmentIataCode": "321",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "J",
    "Y"
   ],
   "trafficRestrictions": [
    "X"
   ],
   "operator": {
    "carrierFsCode": "B6",
    "flightNumber": "690",
    "serviceType": "J",
    "serviceClasses": [
     "R",
     "F",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-2419370--2419850"
  },
  {
   "carrierFsCode": "B6",
   "flightNumber": "1802",
   "departureAirportFsCode": "FLL",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "departureTerminal": "3",
   "arrivalTerminal": "5",
   "departureTime": "2017-02-09T21:46:00.000",
   "arrivalTime": "2017-02-10T00:26:00.000",
   "flightEquipmentIataCode": "320",
   "isCodeshare": False,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "R",
    "F",
    "J",
    "Y"
   ],
   "trafficRestrictions": [],
   "codeshares": [
    {
     "carrierFsCode": "HA",
     "flightNumber": "2083",
     "serviceType": "J",
     "serviceClasses": [
      "J",
      "Y"
     ],
     "trafficRestrictions": [
      "X"
     ],
     "referenceCode": 1383290
    },
    {
     "carrierFsCode": "QR",
     "flightNumber": "4208",
     "serviceType": "J",
     "serviceClasses": [
      "Y"
     ],
     "trafficRestrictions": [
      "Y"
     ],
     "referenceCode": 10575935
    }
   ],
   "referenceCode": "29-1383515--"
  },
  {
   "carrierFsCode": "HA",
   "flightNumber": "2083",
   "departureAirportFsCode": "FLL",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "departureTerminal": "3",
   "arrivalTerminal": "5",
   "departureTime": "2017-02-09T21:46:00.000",
   "arrivalTime": "2017-02-10T00:26:00.000",
   "flightEquipmentIataCode": "320",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "J",
    "Y"
   ],
   "trafficRestrictions": [
    "X"
   ],
   "operator": {
    "carrierFsCode": "B6",
    "flightNumber": "1802",
    "serviceType": "J",
    "serviceClasses": [
     "R",
     "F",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-1383515--1383290"
  },
  {
   "carrierFsCode": "QR",
   "flightNumber": "4208",
   "departureAirportFsCode": "FLL",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "departureTerminal": "3",
   "arrivalTerminal": "5",
   "departureTime": "2017-02-09T21:46:00.000",
   "arrivalTime": "2017-02-10T00:26:00.000",
   "flightEquipmentIataCode": "320",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "Y"
   ],
   "trafficRestrictions": [
    "Y"
   ],
   "operator": {
    "carrierFsCode": "B6",
    "flightNumber": "1802",
    "serviceType": "J",
    "serviceClasses": [
     "R",
     "F",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-1383515--10575935"
  },
  {
   "carrierFsCode": "B6",
   "flightNumber": "916",
   "departureAirportFsCode": "SFO",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "departureTerminal": "I",
   "arrivalTerminal": "5",
   "departureTime": "2017-02-09T15:55:00.000",
   "arrivalTime": "2017-02-10T00:19:00.000",
   "flightEquipmentIataCode": "32S",
   "isCodeshare": False,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "R",
    "F",
    "J",
    "Y"
   ],
   "trafficRestrictions": [],
   "codeshares": [],
   "referenceCode": "29-3463253--"
  },
  {
   "carrierFsCode": "AA",
   "flightNumber": "180",
   "departureAirportFsCode": "LAX",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "8",
   "departureTime": "2017-02-09T16:30:00.000",
   "arrivalTime": "2017-02-10T00:58:00.000",
   "flightEquipmentIataCode": "32B",
   "isCodeshare": False,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "F",
    "J",
    "Y"
   ],
   "trafficRestrictions": [],
   "codeshares": [
    {
     "carrierFsCode": "QF",
     "flightNumber": "3087",
     "serviceType": "J",
     "serviceClasses": [
      "F",
      "J",
      "Y"
     ],
     "trafficRestrictions": [
      "Q"
     ],
     "referenceCode": 10883100
    },
    {
     "carrierFsCode": "HU",
     "flightNumber": "8907",
     "serviceType": "J",
     "serviceClasses": [
      "F",
      "J",
      "Y"
     ],
     "trafficRestrictions": [
      "O"
     ],
     "referenceCode": 10883102
    },
    {
     "carrierFsCode": "TN",
     "flightNumber": "1214",
     "serviceType": "J",
     "serviceClasses": [
      "J",
      "Y"
     ],
     "trafficRestrictions": [
      "Q"
     ],
     "referenceCode": 10883104
    },
    {
     "carrierFsCode": "AS",
     "flightNumber": "6394",
     "serviceType": "J",
     "serviceClasses": [
      "R",
      "F",
      "Y"
     ],
     "trafficRestrictions": [],
     "referenceCode": 10883106
    },
    {
     "carrierFsCode": "EY",
     "flightNumber": "3029",
     "serviceType": "J",
     "serviceClasses": [
      "R",
      "F",
      "J",
      "Y"
     ],
     "trafficRestrictions": [
      "G"
     ],
     "referenceCode": 10883108
    },
    {
     "carrierFsCode": "BA",
     "flightNumber": "7774",
     "serviceType": "J",
     "serviceClasses": [
      "R",
      "F",
      "J",
      "Y"
     ],
     "trafficRestrictions": [
      "Q"
     ],
     "referenceCode": 10883110
    }
   ],
   "referenceCode": "29-2036019--"
  },
  {
   "carrierFsCode": "QF",
   "flightNumber": "3087",
   "departureAirportFsCode": "LAX",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "8",
   "departureTime": "2017-02-09T16:30:00.000",
   "arrivalTime": "2017-02-10T00:58:00.000",
   "flightEquipmentIataCode": "32B",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "F",
    "J",
    "Y"
   ],
   "trafficRestrictions": [
    "Q"
   ],
   "operator": {
    "carrierFsCode": "AA",
    "flightNumber": "180",
    "serviceType": "J",
    "serviceClasses": [
     "F",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-2036019--10883100"
  },
  {
   "carrierFsCode": "HU",
   "flightNumber": "8907",
   "departureAirportFsCode": "LAX",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "8",
   "departureTime": "2017-02-09T16:30:00.000",
   "arrivalTime": "2017-02-10T00:58:00.000",
   "flightEquipmentIataCode": "32B",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "F",
    "J",
    "Y"
   ],
   "trafficRestrictions": [
    "O"
   ],
   "operator": {
    "carrierFsCode": "AA",
    "flightNumber": "180",
    "serviceType": "J",
    "serviceClasses": [
     "F",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-2036019--10883102"
  },
  {
   "carrierFsCode": "TN",
   "flightNumber": "1214",
   "departureAirportFsCode": "LAX",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "8",
   "departureTime": "2017-02-09T16:30:00.000",
   "arrivalTime": "2017-02-10T00:58:00.000",
   "flightEquipmentIataCode": "32B",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "J",
    "Y"
   ],
   "trafficRestrictions": [
    "Q"
   ],
   "operator": {
    "carrierFsCode": "AA",
    "flightNumber": "180",
    "serviceType": "J",
    "serviceClasses": [
     "F",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-2036019--10883104"
  },
  {
   "carrierFsCode": "AS",
   "flightNumber": "6394",
   "departureAirportFsCode": "LAX",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "8",
   "departureTime": "2017-02-09T16:30:00.000",
   "arrivalTime": "2017-02-10T00:58:00.000",
   "flightEquipmentIataCode": "32B",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "R",
    "F",
    "Y"
   ],
   "trafficRestrictions": [],
   "operator": {
    "carrierFsCode": "AA",
    "flightNumber": "180",
    "serviceType": "J",
    "serviceClasses": [
     "F",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-2036019--10883106"
  },
  {
   "carrierFsCode": "EY",
   "flightNumber": "3029",
   "departureAirportFsCode": "LAX",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "8",
   "departureTime": "2017-02-09T16:30:00.000",
   "arrivalTime": "2017-02-10T00:58:00.000",
   "flightEquipmentIataCode": "32B",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "R",
    "F",
    "J",
    "Y"
   ],
   "trafficRestrictions": [
    "G"
   ],
   "operator": {
    "carrierFsCode": "AA",
    "flightNumber": "180",
    "serviceType": "J",
    "serviceClasses": [
     "F",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-2036019--10883108"
  },
  {
   "carrierFsCode": "BA",
   "flightNumber": "7774",
   "departureAirportFsCode": "LAX",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "8",
   "departureTime": "2017-02-09T16:30:00.000",
   "arrivalTime": "2017-02-10T00:58:00.000",
   "flightEquipmentIataCode": "32B",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "R",
    "F",
    "J",
    "Y"
   ],
   "trafficRestrictions": [
    "Q"
   ],
   "operator": {
    "carrierFsCode": "AA",
    "flightNumber": "180",
    "serviceType": "J",
    "serviceClasses": [
     "F",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-2036019--10883110"
  },
  {
   "carrierFsCode": "AA",
   "flightNumber": "1406",
   "departureAirportFsCode": "MIA",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "8",
   "departureTime": "2017-02-09T21:56:00.000",
   "arrivalTime": "2017-02-10T00:51:00.000",
   "flightEquipmentIataCode": "73H",
   "isCodeshare": False,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "R",
    "J",
    "Y"
   ],
   "trafficRestrictions": [],
   "codeshares": [
    {
     "carrierFsCode": "JJ",
     "flightNumber": "2334",
     "serviceType": "J",
     "serviceClasses": [
      "J",
      "Y"
     ],
     "trafficRestrictions": [
      "G"
     ],
     "referenceCode": 2546848
    },
    {
     "carrierFsCode": "LA",
     "flightNumber": "8715",
     "serviceType": "J",
     "serviceClasses": [
      "J",
      "Y"
     ],
     "trafficRestrictions": [
      "G"
     ],
     "referenceCode": 11130045
    },
    {
     "carrierFsCode": "MH",
     "flightNumber": "9439",
     "serviceType": "J",
     "serviceClasses": [
      "J",
      "Y"
     ],
     "trafficRestrictions": [
      "O"
     ],
     "referenceCode": 11130046
    },
    {
     "carrierFsCode": "BA",
     "flightNumber": "4373",
     "serviceType": "J",
     "serviceClasses": [
      "R",
      "J",
      "Y"
     ],
     "trafficRestrictions": [
      "Q"
     ],
     "referenceCode": 11130047
    }
   ],
   "referenceCode": "29-2547400--"
  },
  {
   "carrierFsCode": "JJ",
   "flightNumber": "2334",
   "departureAirportFsCode": "MIA",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "8",
   "departureTime": "2017-02-09T21:56:00.000",
   "arrivalTime": "2017-02-10T00:51:00.000",
   "flightEquipmentIataCode": "73H",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "J",
    "Y"
   ],
   "trafficRestrictions": [
    "G"
   ],
   "operator": {
    "carrierFsCode": "AA",
    "flightNumber": "1406",
    "serviceType": "J",
    "serviceClasses": [
     "R",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-2547400--2546848"
  },
  {
   "carrierFsCode": "LA",
   "flightNumber": "8715",
   "departureAirportFsCode": "MIA",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "8",
   "departureTime": "2017-02-09T21:56:00.000",
   "arrivalTime": "2017-02-10T00:51:00.000",
   "flightEquipmentIataCode": "73H",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "J",
    "Y"
   ],
   "trafficRestrictions": [
    "G"
   ],
   "operator": {
    "carrierFsCode": "AA",
    "flightNumber": "1406",
    "serviceType": "J",
    "serviceClasses": [
     "R",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-2547400--11130045"
  },
  {
   "carrierFsCode": "MH",
   "flightNumber": "9439",
   "departureAirportFsCode": "MIA",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "8",
   "departureTime": "2017-02-09T21:56:00.000",
   "arrivalTime": "2017-02-10T00:51:00.000",
   "flightEquipmentIataCode": "73H",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "J",
    "Y"
   ],
   "trafficRestrictions": [
    "O"
   ],
   "operator": {
    "carrierFsCode": "AA",
    "flightNumber": "1406",
    "serviceType": "J",
    "serviceClasses": [
     "R",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-2547400--11130046"
  },
  {
   "carrierFsCode": "BA",
   "flightNumber": "4373",
   "departureAirportFsCode": "MIA",
   "arrivalAirportFsCode": "JFK",
   "stops": 0,
   "arrivalTerminal": "8",
   "departureTime": "2017-02-09T21:56:00.000",
   "arrivalTime": "2017-02-10T00:51:00.000",
   "flightEquipmentIataCode": "73H",
   "isCodeshare": True,
   "isWetlease": False,
   "serviceType": "J",
   "serviceClasses": [
    "R",
    "J",
    "Y"
   ],
   "trafficRestrictions": [
    "Q"
   ],
   "operator": {
    "carrierFsCode": "AA",
    "flightNumber": "1406",
    "serviceType": "J",
    "serviceClasses": [
     "R",
     "J",
     "Y"
    ],
    "trafficRestrictions": []
   },
   "codeshares": [],
   "referenceCode": "29-2547400--11130047"
  }
 ],
 "appendix": {
  "airlines": [
   {
    "fs": "AA",
    "iata": "AA",
    "icao": "AAL",
    "name": "American Airlines",
    "phoneNumber": "08457-567-567",
    "active": True
   },
   {
    "fs": "JJ",
    "iata": "JJ",
    "icao": "TAM",
    "name": "LATAM Airlines Brasil",
    "phoneNumber": "1-888-2FLY TAM",
    "active": True
   },
   {
    "fs": "QR",
    "iata": "QR",
    "icao": "QTR",
    "name": "Qatar Airways",
    "phoneNumber": "+1 877 777 2827",
    "active": True
   },
   {
    "fs": "EK",
    "iata": "EK",
    "icao": "UAE",
    "name": "Emirates",
    "phoneNumber": "800 777 3999",
    "active": True
   },
   {
    "fs": "DL",
    "iata": "DL",
    "icao": "DAL",
    "name": "Delta Air Lines",
    "phoneNumber": "1-800-221-1212",
    "active": True
   },
   {
    "fs": "VA",
    "iata": "VA",
    "icao": "VOZ",
    "name": "Virgin Australia",
    "active": True
   },
   {
    "fs": "HU",
    "iata": "HU",
    "icao": "CHH",
    "name": "Hainan Airlines",
    "phoneNumber": "03-10-2007",
    "active": True
   },
   {
    "fs": "SA",
    "iata": "SA",
    "icao": "SAA",
    "name": "South African Airways",
    "phoneNumber": "+27 11 978 5313",
    "active": True
   },
   {
    "fs": "AS",
    "iata": "AS",
    "icao": "ASA",
    "name": "Alaska Airlines",
    "phoneNumber": "1-800-252-7522",
    "active": True
   },
   {
    "fs": "B6",
    "iata": "B6",
    "icao": "JBU",
    "name": "JetBlue Airways",
    "phoneNumber": "1-800-538-2583",
    "active": True
   },
   {
    "fs": "EY",
    "iata": "EY",
    "icao": "ETD",
    "name": "Etihad Airways",
    "active": True
   },
   {
    "fs": "QF",
    "iata": "QF",
    "icao": "QFA",
    "name": "Qantas",
    "phoneNumber": "+61 2 9691 3636",
    "active": True
   },
   {
    "fs": "LA",
    "iata": "LA",
    "icao": "LAN",
    "name": "LATAM Airlines",
    "phoneNumber": "1 (305) 670 9999",
    "active": True
   },
   {
    "fs": "AZ",
    "iata": "AZ",
    "icao": "AZA",
    "name": "Alitalia",
    "phoneNumber": "1-800-223-5730",
    "active": True
   },
   {
    "fs": "HA",
    "iata": "HA",
    "icao": "HAL",
    "name": "Hawaiian Airlines",
    "phoneNumber": "1-800-367-5320",
    "active": True
   },
   {
    "fs": "KE",
    "iata": "KE",
    "icao": "KAL",
    "name": "Korean Air",
    "phoneNumber": "1-800-438-5000",
    "active": True
   },
   {
    "fs": "TN",
    "iata": "TN",
    "icao": "THT",
    "name": "Air Tahiti Nui",
    "active": True
   },
   {
    "fs": "Y4",
    "iata": "Y4",
    "icao": "VOI",
    "name": "Volaris",
    "active": True
   },
   {
    "fs": "MH",
    "iata": "MH",
    "icao": "MAS",
    "name": "Malaysia Airlines",
    "phoneNumber": "+603 7843 3000",
    "active": True
   },
   {
    "fs": "VS",
    "iata": "VS",
    "icao": "VIR",
    "name": "Virgin Atlantic",
    "active": True
   },
   {
    "fs": "BA",
    "iata": "BA",
    "icao": "BAW",
    "name": "British Airways",
    "phoneNumber": "1-800-AIRWAYS",
    "active": True
   }
  ],
  "airports": [
   {
    "fs": "LAX",
    "iata": "LAX",
    "icao": "KLAX",
    "faa": "LAX",
    "name": "Los Angeles International Airport",
    "street1": "One World Way",
    "street2": "",
    "city": "Los Angeles",
    "cityCode": "LAX",
    "stateCode": "CA",
    "postalCode": "90045-5803",
    "countryCode": "US",
    "countryName": "United States",
    "regionName": "North America",
    "timeZoneRegionName": "America/Los_Angeles",
    "weatherZone": "CAZ041",
    "localTime": "2017-02-10T22:44:59.026",
    "utcOffsetHours": -8,
    "latitude": 33.943399,
    "longitude": -118.408279,
    "elevationFeet": 126,
    "classification": 1,
    "active": True
   },
   {
    "fs": "TPA",
    "iata": "TPA",
    "icao": "KTPA",
    "faa": "TPA",
    "name": "Tampa International Airport",
    "street1": "5507 West Spruce Street",
    "city": "Tampa",
    "cityCode": "TPA",
    "stateCode": "FL",
    "postalCode": "33607",
    "countryCode": "US",
    "countryName": "United States",
    "regionName": "North America",
    "timeZoneRegionName": "America/New_York",
    "weatherZone": "FLZ251",
    "localTime": "2017-02-11T01:44:59.026",
    "utcOffsetHours": -5,
    "latitude": 27.979869,
    "longitude": -82.535415,
    "elevationFeet": 26,
    "classification": 1,
    "active": True
   },
   {
    "fs": "MIA",
    "iata": "MIA",
    "icao": "KMIA",
    "faa": "MIA",
    "name": "Miami International Airport",
    "street1": "4200 N.W. 21 Street",
    "street2": "",
    "city": "Miami",
    "cityCode": "MIA",
    "stateCode": "FL",
    "postalCode": "33122",
    "countryCode": "US",
    "countryName": "United States",
    "regionName": "North America",
    "timeZoneRegionName": "America/New_York",
    "weatherZone": "FLZ074",
    "localTime": "2017-02-11T01:44:59.027",
    "utcOffsetHours": -5,
    "latitude": 25.796,
    "longitude": -80.278234,
    "elevationFeet": 8,
    "classification": 1,
    "active": True
   },
   {
    "fs": "FLL",
    "iata": "FLL",
    "icao": "KFLL",
    "faa": "FLL",
    "name": "Fort Lauderdale-Hollywood International Airport",
    "street1": "320 Terminal Drive",
    "city": "Fort Lauderdale",
    "cityCode": "FLL",
    "stateCode": "FL",
    "countryCode": "US",
    "countryName": "United States",
    "regionName": "North America",
    "timeZoneRegionName": "America/New_York",
    "weatherZone": "FLZ072",
    "localTime": "2017-02-11T01:44:59.026",
    "utcOffsetHours": -5,
    "latitude": 26.071492,
    "longitude": -80.144908,
    "elevationFeet": 9,
    "classification": 1,
    "active": True
   },
   {
    "fs": "JFK",
    "iata": "JFK",
    "icao": "KJFK",
    "faa": "JFK",
    "name": "John F. Kennedy International Airport",
    "street1": "JFK Airport",
    "city": "New York",
    "cityCode": "NYC",
    "stateCode": "NY",
    "postalCode": "11430",
    "countryCode": "US",
    "countryName": "United States",
    "regionName": "North America",
    "timeZoneRegionName": "America/New_York",
    "weatherZone": "NYZ178",
    "localTime": "2017-02-11T01:44:58.980",
    "utcOffsetHours": -5,
    "latitude": 40.642335,
    "longitude": -73.78817,
    "elevationFeet": 13,
    "classification": 1,
    "active": True
   },
   {
    "fs": "GDL",
    "iata": "GDL",
    "icao": "MMGL",
    "name": "Don Miguel Hidal Y Costilla International Airport",
    "city": "Guadalajara",
    "cityCode": "GDL",
    "countryCode": "MX",
    "countryName": "Mexico",
    "regionName": "North America",
    "timeZoneRegionName": "America/Mexico_City",
    "localTime": "2017-02-11T00:44:59.026",
    "utcOffsetHours": -6,
    "latitude": 20.525986,
    "longitude": -103.303984,
    "elevationFeet": 5022,
    "classification": 2,
    "active": True
   },
   {
    "fs": "MCO",
    "iata": "MCO",
    "icao": "KMCO",
    "faa": "MCO",
    "name": "Orlando International Airport",
    "street1": "One Airport Boulevard",
    "street2": "",
    "city": "Orlando",
    "cityCode": "ORL",
    "stateCode": "FL",
    "postalCode": "32827-4399",
    "countryCode": "US",
    "countryName": "United States",
    "regionName": "North America",
    "timeZoneRegionName": "America/New_York",
    "weatherZone": "FLZ045",
    "localTime": "2017-02-11T01:44:59.026",
    "utcOffsetHours": -5,
    "latitude": 28.432177,
    "longitude": -81.308301,
    "elevationFeet": 96,
    "classification": 1,
    "active": True
   },
   {
    "fs": "SFO",
    "iata": "SFO",
    "icao": "KSFO",
    "faa": "SFO",
    "name": "San Francisco International Airport",
    "city": "San Francisco",
    "cityCode": "SFO",
    "stateCode": "CA",
    "postalCode": "94128",
    "countryCode": "US",
    "countryName": "United States",
    "regionName": "North America",
    "timeZoneRegionName": "America/Los_Angeles",
    "weatherZone": "CAZ508",
    "localTime": "2017-02-10T22:44:59.026",
    "utcOffsetHours": -8,
    "latitude": 37.615215,
    "longitude": -122.389881,
    "elevationFeet": 11,
    "classification": 1,
    "active": True
   }
  ],
  "equipments": [
   {
    "iata": "32B",
    "name": "Airbus A321 (sharklets)",
    "turboProp": False,
    "jet": True,
    "widebody": False,
    "regional": False
   },
   {
    "iata": "73H",
    "name": "Boeing 737-800 (winglets) Passenger/BBJ2",
    "turboProp": False,
    "jet": True,
    "widebody": False,
    "regional": False
   },
   {
    "iata": "320",
    "name": "Airbus A320",
    "turboProp": False,
    "jet": True,
    "widebody": False,
    "regional": False
   },
   {
    "iata": "321",
    "name": "Airbus A321",
    "turboProp": False,
    "jet": True,
    "widebody": False,
    "regional": False
   },
   {
    "iata": "32S",
    "name": "Airbus A318 / A319 / A320 / A321",
    "turboProp": False,
    "jet": True,
    "widebody": False,
    "regional": False
   },
   {
    "iata": "75W",
    "name": "Boeing 757-200 (winglets) Passenger",
    "turboProp": False,
    "jet": True,
    "widebody": False,
    "regional": False
   }
  ]
 }
}


HOST = "localhost"
DATABASE = "revmax_development"
USER = "nandukalidindi"
PASSWORD = "qwerty123"

AIRPORT_LIST = ['JFK', 'LGA', 'EWR']

FLIGHT_STATS_API = "https://api.flightstats.com/flex"
SCHEDULES = "schedules/rest/v1/json/to"
APP_ID = "8146b8bf"
APP_KEY = "c5a75fe109e3f3cb61a8789422d5b45e"

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

# def persist_flight_arrivals_till_date(airport, year, month, day):


def persist_flight_arrivals_for_a_day(airport, year, month, day):
    for hour in range(0, 24):
        get_flight_arrivals(airport, year, month, day, hour)


def get_flight_arrivals(airport, year, month, day, hour):
    # arrival_response = requests.get(build_flight_stat_url_for_particular_hour(airport, year, month, day, hour))
    # print(arrival_response.json())
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
get_flight_arrivals('JFK', 2017, 2, 10, 0)
pg_connection.commit()
pg_connection.close()
