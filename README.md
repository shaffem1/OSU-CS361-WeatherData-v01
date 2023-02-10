# OSU-CS361-WeatherData-v01

Communications contract
Requests - Data is requested using different gRPC unary methods. There are 8 different methods available:

MaxTemp
MinTemp
DaysBelowFreezing
MaxWindGust
WindyDays
AvgDailyPrecip
AnnualSnowDepth
AnnualRainfall

An example of a call:

    loc = weatherStation
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.MaxTemp(helloworld_pb2.MaxTempRequest(name=loc))
        print("The record high temperature for ", weatherStation, " is ", response.message, "F")

Receiving - Data is received in 8 different response methods, these are:

MaxTempReply
MinTempReply
DaysBelowFreezingReply
MaxWindGustReply
WindyDaysReply
AvgDailyPrecipReply
AnnualSnowDepthReply
AnnualRainfallReply

The following line of code stores the data from the response method in a variable so it can be used in the client program:

 response = stub.MaxTemp(helloworld_pb2.MaxTempRequest(name=loc))



![cs361-uml-diagram](https://user-images.githubusercontent.com/29556835/218222175-d4ccd431-8e33-4b93-9c74-2bd56a7e5dae.jpg)

