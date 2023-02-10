
from concurrent import futures
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
      if(request.name == "KIAD"):
        return helloworld_pb2.HelloReply(message='10')
      elif(request.name == "KSFO"):
        return helloworld_pb2.HelloReply(message='45')
      elif(request.name == "KDCA"):
        return helloworld_pb2.HelloReply(message='-2')

    def MaxTemp(self, request, context):
      if(request.name == "KIAD"):
        return helloworld_pb2.MaxTempReply(message='102')
      elif(request.name == "KSFO"):
        return helloworld_pb2.MaxTempReply(message='95')
      elif(request.name == "KDCA"):
        return helloworld_pb2.MaxTempReply(message='105')

    def DaysBelowFreezing(self, request, context):
      if(request.name == "KIAD"):
        return helloworld_pb2.DaysBelowFreezingReply(message='45')
      elif(request.name == "KSFO"):
        return helloworld_pb2.DaysBelowFreezingReply(message='0')
      elif(request.name == "KDCA"):
        return helloworld_pb2.DaysBelowFreezingReply(message='39')

    def MaxWindGust(self, request, context):
      if(request.name == "KIAD"):
        return helloworld_pb2.MaxWindGustReply(message='85')
      elif(request.name == "KSFO"):
        return helloworld_pb2.MaxWindGustReply(message='63')
      elif(request.name == "KDCA"):
        return helloworld_pb2.MaxWindGustReply(message='77')

    def WindyDays(self, request, context):
      if(request.name == "KIAD"):
        return helloworld_pb2.WindyDaysReply(message='72')
      elif(request.name == "KSFO"):
        return helloworld_pb2.WindyDaysReply(message='45')
      elif(request.name == "KDCA"):
        return helloworld_pb2.WindyDaysReply(message='79')

    def AvgDailyPrecip(self, request, context):
      if(request.name == "KIAD"):
        return helloworld_pb2.AvgDailyPrecipReply(message='.2')
      elif(request.name == "KSFO"):
        return helloworld_pb2.AvgDailyPrecipReply(message='.8')
      elif(request.name == "KDCA"):
        return helloworld_pb2.AvgDailyPrecipReply(message='.21')

    def AnnualSnowDepth(self, request, context):
      if(request.name == "KIAD"):
        return helloworld_pb2.AnnualSnowDepthReply(message='12.4')
      elif(request.name == "KSFO"):
        return helloworld_pb2.AnnualSnowDepthReply(message='0')
      elif(request.name == "KDCA"):
        return helloworld_pb2.AnnualSnowDepthReply(message='10.2')

    def AnnualRainfall(self, request, context):
      if(request.name == "KIAD"):
        return helloworld_pb2.AnnualRainfallReply(message='45.2')
      elif(request.name == "KSFO"):
        return helloworld_pb2.AnnualRainfallReply(message='83.7')
      elif(request.name == "KDCA"):
        return helloworld_pb2.AnnualRainfallReply(message='43.4')


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
