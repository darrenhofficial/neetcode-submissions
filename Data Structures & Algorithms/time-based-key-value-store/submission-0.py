class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key,[])
        res = ""
        L , R = 0 , len(values) - 1
        while L <=R:
            mid = (L + R) //2
            if values [mid][0] <= timestamp:
                res = values[mid][1]
                L = mid + 1
            else : R = mid -1
        return res

        
