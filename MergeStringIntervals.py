class Solution:
    def mergeIntervals(self, intervals: list):
        local_min = 0
        local_max = 0
        ranges = []
        enumerate_intervals = enumerate(intervals)

        for interval in intervals:
            split = interval.split('-')
            i_min_value = int(split[0])
            i_max_value = int(split[1])

            for interval2 in intervals:
                split = interval2.split('-')
                i2_min_value = int(split[0])
                i2_max_value = int(split[1])
                i2_range = range(i2_min_value, i2_max_value)
                if i2_min_value == i_min_value and i2_max_value == i_max_value:
                    continue

                if i_min_value not in i2_range and i_max_value not in i2_range:
                    str_value = str(i2_min_value) + '-' + str(i2_max_value)
                    if str_value not in ranges:
                        ranges.append(str_value)
                    continue

                local_min = min(i_min_value, i2_min_value)
                local_max = max(i_max_value, i2_max_value)
                str_value = str(local_min) + '-' + str(local_max)
                if str_value not in ranges:
                    ranges.append(str_value)

        return ranges


cases = [
    ['2-4', '7-10', '3-5'],
    ['1-3', '3-5', '6-7', '2-4'],
    ['1-5', '1-10', '1-20'],
    ['1-5', '2-4', '7-9'],
    ['2-5', '7-10']
]

for case in cases:
    print(Solution().mergeIntervals(intervals=case))
