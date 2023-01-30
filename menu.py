import sys
import os

currentMenu = 0
weatherStation = 0
option = 0
mode = 0
temperatureSelection = 0
wxStations = {
  "1": "KIAD",
  "2": "KORD",
  "3": "KSFO"
}

def menu1():
    global wxStations
    global weatherStation
    global option
    while(True):
        print("")
        print("Hello! Welcome to the climate data lookup tool. ")
        print("This tool will display some weather statistics for")
        print("a location. ")
        print("New feature! We now have snow data for each location.")
        print("First off, please select your location (1-3). You may")
        print("also enter the letters of the station:")
        print("1 - KIAD - Dulles Airport")
        print("2 - KORD - Chicago O'Hare")
        print("3 - KSFO - San Francisco Airport")
        print("4 - Exit program")
        temp = input('Enter a selection (1-4): ')
        if(temp == "KIAD"):
            weatherStation = 1
        elif(temp == "KORD"):
            weatherStation = 2
        elif(temp == "KSFO"):
            weatherStation = 3
        elif(temp == "4"):
            print("Do you really want to quit? ")
            input("Press Enter to quit...")
            os.quit
        else:
            weatherStation = int(temp)
        st = str(weatherStation)

        selectMode()

        if(mode == 1):
            tempDataMenu()
        elif(mode == 2):
            windDataMenu()
        elif(mode == 3):
            precipDataMenu()
        elif(mode == 5):
            return

def selectMode():
    global mode
    global weatherStation
    st = str(weatherStation)
    print("")
    print("Thanks, you selected station", wxStations[st])
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
    recordLow = "-12"
    recordHigh = "103"
    daysBelowFreezing = 23
    st = str(weatherStation)
    print("")
    print("You have chosen to view temperature data for station ", wxStations[st])
    print("Choose the weather data you want displayed: ")
    print("1 - Record low temperature")
    print("2 - Record high temperature")
    print("3 - Days below freezing")
    print("4 - Return to Main Menu")
    temperatureSelection = int(input("Enter a selection (1-4): "))
    if(temperatureSelection == 1):
        print("The record low temperature for ",weatherStation," is ", recordLow,"F.")
        input("Press Enter to continue...")
    elif(temperatureSelection == 2):
        print("The record high temperature for ",weatherStation," is", recordHigh,"F.")
        input("Press Enter to continue...")
    elif(temperatureSelection == 3):
        print("The annual days below freezing for ",weatherStation," is", daysBelowFreezing," days.")
        input("Press Enter to continue...")
    elif(temperatureSelection == 4):
        return
    elif (temperatureSelection == 5):
        print("Do you really want to quit? ")
        input("Press Enter to quit...")
        os.quit
    tempDataMenu()

def windDataMenu():
    global weatherStation
    maxWindGust = "84"
    recordHigh = "103"
    daysBelowFreezing = 23
    st = str(weatherStation)
    print("")
    print("You have chosen to view wind data for station ", wxStations[st])
    print("Choose the weather data you want displayed: ")
    print("1 - Maximum wind gust")
    print("2 - Days with wind above 40mph")
    print("3 - Return to Main Menu")
    windSelection = int(input("Enter a selection (1-4): "))
    if(windSelection == 1):
        print("The maximum wind gust for ",wxStations[st]," is ", maxWindGust,"mph.")
        input("Press Enter to continue...")
    elif(windSelection == 2):
        print("The number of days above 40mph for ",wxStations[st]," is", 34,".")
        input("Press Enter to continue...")
    elif(windSelection == 3):
        return
    windDataMenu()

def precipDataMenu():
    global weatherStation
    st = str(weatherStation)
    avgDailyPrecip = ".5"
    annualSnowDepth = "12"
    annualRainfall = 23
    print("")
    print("You have chosen to view precipitation data for station ", wxStations[st])
    print("Choose the weather data you want displayed: ")
    print("1 - Average daily precipitation")
    print("2 - Annual snow depth")
    print("3 - Annual rain amount")
    print("4 - Return to Main Menu")
    precipSelection = int(input("Enter a selection (1-4): "))
    if (precipSelection == 1):
        print("The average daily precipitation for ", wxStations[st], " is ", avgDailyPrecip, "inches.")
        input("Press Enter to continue...")
    elif (precipSelection == 2):
        print("The annual snow depth for ", wxStations[st], " is", annualSnowDepth, "inches.")
        input("Press Enter to continue...")
    elif (precipSelection == 3):
        print("The annual rainfall for ", wxStations[st], " is", annualRainfall, "inches.")
        input("Press Enter to continue...")
    elif (precipSelection == 4):
        return
    precipDataMenu()

menu1()