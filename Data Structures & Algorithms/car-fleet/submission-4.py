class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        n = len(speed)
        for i in range(n):
            cars.append([position[i], (target-position[i])/speed[i]]) #pos, arrival time

        # sort cars sublists on position on road.
        cars.sort(key=lambda x: x[0])  
        
        latest_arrival_time = cars[n-1][1]
        fleet_count = 1
        for car in cars[-2::-1]: #iterate from n-1 to 0 O(n)
            #same fleet, either same arrival time, or joint fleet on the road
            if car[1] <= latest_arrival_time:
                fleet_count += 0

            # car arrives later then previous fleet
            if car[1] > latest_arrival_time:
                fleet_count += 1
                latest_arrival_time = car[1]

        return fleet_count        
