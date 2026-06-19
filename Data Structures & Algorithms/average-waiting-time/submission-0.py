class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # i.e. customers = [[1,2],[2,5],[4,3]]
        # [1, 2]
            # 1 = arrival, 2 = time to cook
        # chef completes orders in order
            # arrival in non-decreasing
                # duplicate arrivals possible
                # still complete one at time
                    # looking at orders left -> right
        
        # each ticket in cusotmer map to wait time
            # get average of that result wait times
    
        wait = [0] * len(customers)
        time = customers[0][0] # first arrival

        for i, (arrv, cook) in enumerate(customers):
            time = max(time, arrv)
            time += cook
            wait[i] = time - arrv

        return sum(wait) / len(wait)