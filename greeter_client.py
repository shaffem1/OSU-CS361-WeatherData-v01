
from __future__ import print_function

import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import sys
import os

currentMenu = 0
weatherStation = 0
option = 0
mode = 0
temperatureSelection = 0
wxStations = {
  "1": "KIAD",
  "2": "KSFO",
  "3": "KDCA"
}

def menu1():
  global weatherStation
  global option
  while (True):
    print("")
    print("Hello! Welcome to the climate data lookup tool. ")
    print("This tool will display some weather statistics for")
    print("a location. ")
    print("New feature! We now have snow data for each location.")
    print("First off, please select your location:")
    print("KIAD - Dulles Airport")
    print("KSFO - San Francisco Airport")
    print("KDCA - Washington National Airport")
    print("0 - Exit program")
    temp = input('Enter a selection (1-4): ')
    if (temp == "0"):
      print("Do you really want to quit? ")
      input("Press Enter to quit...")
      os.exit
    else:
      weatherStation = temp

    selectMode()

    if (mode == 1):
      tempDataMenu()
    elif (mode == 2):
      windDataMenu()
    elif (mode == 3):
      precipDataMenu()
    elif (mode == 5):
      return


def selectMode():
  global mode
  global weatherStation
  print("")
  print("Thanks, you selected station", weatherStation)
  print("What type of data would you like to view?")
  print("1 - Display temperature data")
  print("2 - Display wind data")
  print("3 - Display precipitation data")
  print("4 - Return to Main Menu")
  print("5 - Exit program")
  mode = int(input('Enter a selection (1-5): '))


def tempDataMenu():
  global weatherStation
  global temperatureSelection
  print("")
  print("You have chosen to view temperature data for station ", weatherStation)
  print("Choose the weather data you want displayed: ")
  print("1 - Record low temperature")
  print("2 - Record high temperature")
  print("3 - Days below freezing")
  print("4 - Return to Main Menu")
  temperatureSelection = int(input("Enter a selection (1-4): "))
  if (temperatureSelection == 1):
    loc = weatherStation
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name=loc))
        print("The record low temperature for ", weatherStation, " is ", response.message, "F")
    input("Press Enter to continue...")
  elif (temperatureSelection == 2):
    loc = weatherStation
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.MaxTemp(helloworld_pb2.MaxTempRequest(name=loc))
        print("The record high temperature for ", weatherStation, " is ", response.message, "F")
    input("Press Enter to continue...")
  elif (temperatureSelection == 3):
    loc = weatherStation
    with grpc.insecure_channel('localhost:50051') as channel:
      stub = helloworld_pb2_grpc.GreeterStub(channel)
      response = stub.DaysBelowFreezing(helloworld_pb2.DaysBelowFreezingRequest(name=loc))
    print("The annual days below freezing for ", weatherStation, " is", response.message, " days.")
    input("Press Enter to continue...")
  elif (temperatureSelection == 4):
    return
  elif (temperatureSelection == 5):
    print("Do you really want to quit? ")
    input("Press Enter to quit...")
    os.quit
  tempDataMenu()


def windDataMenu():
  global weatherStation
  print("")
  print("You have chosen to view wind data for station ", weatherStation)
  print("Choose the weather data you want displayed: ")
  print("1 - Maximum wind gust")
  print("2 - Days with wind above 40mph")
  print("3 - Return to Main Menu")
  windSelection = int(input("Enter a selection (1-4): "))
  if (windSelection == 1):
    loc = weatherStation
    with grpc.insecure_channel('localhost:50051') as channel:
      stub = helloworld_pb2_grpc.GreeterStub(channel)
      response = stub.MaxWindGust(helloworld_pb2.MaxWindGustRequest(name=loc))
    print("The maximum wind gust for ", weatherStation, " is ", response.message, "mph")
    input("Press Enter to continue...")
  elif (windSelection == 2):
    loc = weatherStation
    with grpc.insecure_channel('localhost:50051') as channel:
      stub = helloworld_pb2_grpc.GreeterStub(channel)
      response = stub.WindyDays(helloworld_pb2.WindyDaysRequest(name=loc))
    print("The number of days above 40mph for ", weatherStation, " is", response.message)
    input("Press Enter to continue...")
  elif (windSelection == 3):
    return
  windDataMenu()


def precipDataMenu():
  global weatherStation
  print("")
  print("You have chosen to view precipitation data for station ", weatherStation)
  print("Choose the weather data you want displayed: ")
  print("1 - Average daily precipitation")
  print("2 - Annual snow depth")
  print("3 - Annual rain amount")
  print("4 - Return to Main Menu")
  precipSelection = int(input("Enter a selection (1-4): "))
  if (precipSelection == 1):
    loc = weatherStation
    with grpc.insecure_channel('localhost:50051') as channel:
      stub = helloworld_pb2_grpc.GreeterStub(channel)
      response = stub.AvgDailyPrecip(helloworld_pb2.AvgDailyPrecipRequest(name=loc))
    print("The average daily precipitation for ", weatherStation, " is ", response.message, "inches.")
    input("Press Enter to continue...")
  elif (precipSelection == 2):
    loc = weatherStation
    with grpc.insecure_channel('localhost:50051') as channel:
      stub = helloworld_pb2_grpc.GreeterStub(channel)
      response = stub.AnnualSnowDepth(helloworld_pb2.AnnualSnowDepthRequest(name=loc))
    print("The annual snow depth for ", weatherStation, " is", response.message, "inches.")
    input("Press Enter to continue...")
  elif (precipSelection == 3):
    loc = weatherStation
    with grpc.insecure_channel('localhost:50051') as channel:
      stub = helloworld_pb2_grpc.GreeterStub(channel)
      response = stub.AnnualRainfall(helloworld_pb2.AnnualRainfallRequest(name=loc))
    print("The annual rainfall for ", weatherStation, " is", response.message, "inches.")
    input("Press Enter to continue...")
  elif (precipSelection == 4):
    return
  precipDataMenu()


if __name__ == '__main__':
    logging.basicConfig()
    menu1()
