from collections import deque
class RecentCounter:

    def __init__(self):
        self.request = deque()


    def ping(self, t: int) -> int:
        self.request.append(t)
        while self.request[0] < t- 3000:
            self.request.popleft()
            print(self.request)
        return len(self.request)


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
obj.ping(1)
obj.ping(100)
obj.ping(3001)
obj.ping(3002)