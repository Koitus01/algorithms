# strings in cases because of concrete task feature
# similar to https://leetcode.com/problems/merge-intervals/description/

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

        for value in intervals:
            v_min = value[0]
            v_max = value[1]

            if result and result[-1][0] <= v_min <= result[-1][1]:
                result[-1][1] = max(v_max, result[-1][1])
            else:
                result.append(value)

        return result

    def split_str(self, interval: str):
        split = interval.split('-')
        i_min_value = int(split[0])
        i_max_value = int(split[1])

        return [i_min_value, i_max_value]

    def union_str(self, min_value: int, max_value: int):
        return str(min_value) + '-' + str(max_value)


cases = [
    ['1-5', '2-4', '7-9'],
    ['3-20', '1-5', '1-10'],

    ['1-3', '3-5', '6-7', '2-4'],
    ['2-4', '7-10', '3-5', '2-3', '1-5'],
    ['1-4', '0-4'],

    ['2-5', '7-10'],
    ['1-3', '2-6', '8-10', '15-18'],
]

for case in cases:
    print(Solution().merge_intervals(intervals=case))
