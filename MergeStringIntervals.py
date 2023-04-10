class Solution:
    def merge_intervals(self, intervals: list):
        local_min = 0
        local_max = 0
        previous_ranges = []
        result = []
        enumerate_intervals = enumerate(intervals)

        for interval in intervals:
            [i_min_value, i_max_value] = self.split_str(interval)
            str_interval = ''

            for r in previous_ranges:
                [r_min_value, r_max_value] = self.split_str(r)
                r_range = range(r_min_value, r_max_value + 1)

                if i_min_value not in r_range:
                    if r_max_value < r_min_value:
                        str_interval = self.union_str(r_min_value, r_max_value)
                    else:
                        str_interval = self.union_str(i_min_value, i_max_value)
                    continue

                str_interval = self.union_str(min(i_min_value, r_min_value), max(i_max_value, r_max_value))
                result.append(str_interval)

            if interval not in previous_ranges:
                previous_ranges.append(interval)
            if str_interval != '' and str_interval not in result:
                result.append(str_interval)

        return result

    def split_str(self, interval: str):
        split = interval.split('-')
        i_min_value = int(split[0])
        i_max_value = int(split[1])

        return [i_min_value, i_max_value]

    def union_str(self, min_value: int, max_value: int):
        return str(min_value) + '-' + str(max_value)


cases = [
    ['2-4', '7-10', '3-5'],
    ['1-3', '3-5', '6-7', '2-4'],
    ['1-5', '1-10', '3-20'],
    ['1-5', '2-4', '7-9'],
    ['2-5', '7-10']
]

for case in cases:
    print(Solution().merge_intervals(intervals=case))
