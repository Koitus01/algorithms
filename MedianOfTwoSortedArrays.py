from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = sorted(nums1 + nums2)
        list_length = len(merged_list)
        is_odd_list = list_length % 2 == 1
        middle_of_list = int(list_length / 2)

        if is_odd_list:
            return merged_list[middle_of_list]

        if list_length <= 2:
            return (merged_list[0] + merged_list[1]) / 2

        return (merged_list[middle_of_list - 1] + merged_list[middle_of_list]) / 2


arrays = [
    [
        [1, 1], [1, 2]
    ],
    [
        [1, 2, 3, 5, 7], [1, 2]
    ],
    [
        [25, 45, 79], [5, 10, 25, 35]
    ],
    [
        [1, 3], [2]
    ],
    [
        [1], [2]
    ],
    [
        [13, 14, 15], [1, 2, 3]
    ],
    [
        [100, 200, 300], []
    ],

]

for nums1, nums2 in arrays:
    print(Solution().findMedianSortedArrays(nums1=nums1, nums2=nums2))
