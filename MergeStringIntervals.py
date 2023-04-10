class Solution:
    def merge_intervals(self, intervals: list):
        #intervals.sort()
        global_min = 0
        global_max = 0
        previous_ranges = []
        result = []

        for interval in intervals:
            [i_min, i_max] = self.split_str(interval)
            result.append([i_min, i_max])

            for index, re in enumerate(result):
                #[re_min, re_max] = self.split_str(re)
                [re_min, re_max] = [re[0], re[1]]
                if i_min == re_min and re_max == i_max:
                    continue

                if re_min <= i_min <= re_max or i_min <= re_min <= i_max:
                    local_min = min(i_min, re_min)
                    local_max = max(i_max, re_max)
                    global_min = min(local_min, global_min)
                    global_max = max(local_max, global_max)

                    if local_min == re_min and local_max == re_max:
                        del result[index]
                        continue
                    if local_min <= re_min <= local_max:
                        del result[index]
                        continue
                    if local_min >= re_min and re_max <= local_max:
                        del result[index]
                        continue

            # if i_min > global_max:
            #     united_str = self.union_str(i_min, i_max)
            #     result.append(united_str)
            #     global_max = i_min

        return result

    def split_str(self, interval: str):
        split = interval.split('-')
        i_min_value = int(split[0])
        i_max_value = int(split[1])

        return [i_min_value, i_max_value]

    def union_str(self, min_value: int, max_value: int):
        return str(min_value) + '-' + str(max_value)


cases = [
    #['1-4', '0-4'],
    ['2-4', '7-10', '3-5'],
    ['1-3', '3-5', '6-7', '2-4'],
    ['1-5', '1-10', '3-20'],
    ['1-5', '2-4', '7-9'],
    ['2-5', '7-10'],
    ['1-3', '2-6', '8-10', '15-18'],
]

for case in cases:
    print(Solution().merge_intervals(intervals=case))
