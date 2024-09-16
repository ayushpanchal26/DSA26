# link - https://bit.ly/3Pld280

from typing import List


class Solution:
    def largest(self, arr : List[int]) -> int:
        # code here
        largest = arr[0]
        for i in arr:
            if i>largest:
                largest = i
        return largest
            