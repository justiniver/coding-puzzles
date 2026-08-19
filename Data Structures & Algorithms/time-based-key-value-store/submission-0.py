from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.time_map[key]:
            return ""
        vals = self.time_map[key]
        l, r = 0, len(vals) - 1
        out = ""
        while l <= r:
            m = l + ((r - l) // 2)
            curr_ts, curr_val = vals[m]

            if curr_ts <= timestamp:
                out = curr_val
                l = m + 1
            else:
                r = m - 1

        return out
