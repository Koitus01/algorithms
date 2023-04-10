class Solution:
    def merge_intervals(self, intervals: list):
        if len(intervals) == 0:
            return []

        if len(intervals) == 1:
            return intervals[0]

        for key, value in enumerate(intervals):
            intervals[key] = self.split_str(value)

        intervals.sort()
        result = []
        global_min = intervals[0][0]
        global_max = 0

        for key, value in enumerate(intervals):
            if key == 0:
                continue

            v_min = value[0]
            v_max = value[1]
            previous_min = intervals[key - 1][0]
            previous_max = intervals[key - 1][1]

            if v_min > previous_max and v_min != previous_min:
                result.append([global_min, global_max])
                global_min = v_min
                result.append([v_min, v_max])

            global_max = max(previous_max, v_max)

        if len(result) == 0:
            result.append([global_min, global_max])

        return result

    def split_str(self, interval: str):
        split = interval.split('-')
        i_min_value = int(split[0])
        i_max_value = int(split[1])

        return [i_min_value, i_max_value]

    def union_str(self, min_value: int, max_value: int):
        return str(min_value) + '-' + str(max_value)


cases = [
    ['3-20', '1-5', '1-10'],
    ['1-3', '3-5', '6-7', '2-4'],
    ['2-4', '7-10', '3-5', '2-3', '1-5'],
    ['1-4', '0-4'],
    ['1-5', '2-4', '7-9'],
    ['2-5', '7-10'],
    ['1-3', '2-6', '8-10', '15-18'],
]

for case in cases:
    print(Solution().merge_intervals(intervals=case))
