class Solution:
    def mergeIntervals(self, intervals: list):
        ranges = []
        for i in intervals:
            splited = i.split('-')

            min_value = int(splited[0])
            max_value = int(splited[1])
            for j in intervals:
                j_splited = j.split('-')
                updated_min_value = j_min_value = int(j_splited[0])
                updated_max_value = j_max_value = int(j_splited[1])
                if min_value is j_min_value and max_value is j_max_value:
                    continue

                j_range = range(j_min_value, j_max_value)
                if min_value in j_range:
                    updated_min_value = min_value

                if max_value in j_range:
                    updated_max_value = max_value

                ranges.append(str(updated_min_value) + '-' + str(updated_max_value))
        return ranges


cases = [
    ['2-4', '7-10', '3-5'],
    ['1-5', '1-10', '1-20'],
    ['1-5', '2-4', '7-9'],
    ['2-5', '7-10']
]

for case in cases:
    print(Solution().mergeIntervals(intervals=case))
