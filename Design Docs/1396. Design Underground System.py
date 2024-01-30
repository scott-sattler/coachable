class UndergroundSystem:
    def __init__(self):
        self.check_in = dict()  # id -> (name, time_in)
        self.time_info = dict()  # name_name -> (total, count)

    # noinspection PyPep8Naming,PyShadowingBuiltins
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    # noinspection PyPep8Naming,PyShadowingBuiltins
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        trip_time = t - self.check_in[id][1]
        trip_name = self.check_in[id][0] + "_" + stationName
        trip_info = self.time_info.get(trip_name, (0.0, 0.0))
        self.time_info[trip_name] = (trip_info[0] + trip_time, trip_info[1] + 1)

    # noinspection PyPep8Naming,PyShadowingBuiltins
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        info = self.time_info[startStation + "_" + endStation]
        return info[0] / info[1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
