from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)

        # Step 1: Frequency of every number
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1

        # Step 2: gcd_count[g] = number of pairs whose gcd is exactly g
        gcd_count = [0] * (max_val + 1)

        # Process gcd values from largest to smallest
        for g in range(max_val, 0, -1):

            # Count how many numbers are divisible by g
            cnt = 0
            for multiple in range(g, max_val + 1, g):
                cnt += freq[multiple]

            # Total pairs divisible by g
            pairs = cnt * (cnt - 1) // 2

            # Remove pairs already counted with larger gcd
            multiple = 2 * g
            while multiple <= max_val:
                pairs -= gcd_count[multiple]
                multiple += g

            gcd_count[g] = pairs

        # Step 3: Prefix counts
        prefix = []
        values = []

        total = 0
        for g in range(1, max_val + 1):
            if gcd_count[g] > 0:
                total += gcd_count[g]
                prefix.append(total)
                values.append(g)

        # Step 4: Answer queries with binary search
        ans = []

        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans