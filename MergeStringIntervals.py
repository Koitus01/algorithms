class Solution:
    def mergeIntervals(self, intervals: list):
        ranges = []
        for i in intervals:
            splited = i.split('-')

            min_value = int(splited[0])
            max_value = int(splited[1])
            for j in intervals:
                j_splited = j.split('-')
                updating_min_value = int(j_splited[0])
                updating_max_value = int(j_splited[1])
                if min_value is updating_min_value and max_value is updating_max_value:
                    continue

                if max_value < updating_min_value:
                    str_interval = str(updating_min_value) + '-' + str(updating_max_value)
                    if str_interval not in ranges:
                        ranges.append(str_interval)

                    continue

                j_range = range(updating_min_value, updating_max_value)
                if min_value in j_range or max_value in j_range:
                    updating_min_value = min_value
                    if max_value > updating_max_value:
                        updating_max_value = max_value
                else:
                    continue

                str_interval = str(updating_min_value) + '-' + str(updating_max_value)
                if str_interval not in ranges:
                    ranges.append(str_interval)
        return ranges


cases = [
    ['2-4', '7-10', '3-5'],
    ['1-5', '1-10', '1-20'],
    ['1-5', '2-4', '7-9'],
    ['2-5', '7-10']
]

for case in cases:
    print(Solution().mergeIntervals(intervals=case))
