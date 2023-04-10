class Solution:
    def merge_intervals(self, intervals: list):
        global_min = 0
        global_max = 0
        previous_ranges = []
        result = []

        for interval in intervals:
            [i_min_value, i_max_value] = self.split_str(interval)
            for r in previous_ranges:
                r_min = r[0]
                r_max = r[1]
                if r_min <= i_min_value <= r_max:
                    local_min = min(i_min_value, r_min)
                    local_max = max(i_max_value, r_max)
                    global_min = min(local_min, global_min)
                    global_max = max(local_max, global_max)
                    for index, re in enumerate(result):
                        [re_min, re_max] = self.split_str(re)
                        if local_min == re_min and local_max == re_max:
                            del result[index]
                            continue
                        if local_min <= re_min <= local_max:
                            del result[index]
                            continue

                    united_str = self.union_str(local_min, local_max)
                    result.append(united_str)

                if r_min > global_max:
                    united_str = self.union_str(r_min, r_max)
                    result.append(united_str)
                    global_max = r_min
                #print(r, r, global_min, global_max)


                    #if len(result) > 1

            if i_min_value > global_max:
                united_str = self.union_str(i_min_value, i_max_value)
                result.append(united_str)
                global_max = i_min_value
            previous_ranges.append([i_min_value, i_max_value])
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
    ['2-5', '7-10'],
    ['1-3', '2-6', '8-10', '15-18']
]

for case in cases:
    print(Solution().merge_intervals(intervals=case))
