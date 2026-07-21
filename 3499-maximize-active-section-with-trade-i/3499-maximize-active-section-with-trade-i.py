class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        original = s.count("1")

        # Add 1 on both ends
        t = "1" + s + "1"

        runs = []

        i = 0
        while i < len(t):

            j = i

            while j < len(t) and t[j] == t[i]:
                j += 1

            runs.append((t[i], j - i))

            i = j

        ans = original

        for i in range(1, len(runs) - 1):

            # Need a 1-run surrounded by 0-runs
            if (
                runs[i][0] == "1"
                and runs[i - 1][0] == "0"
                and runs[i + 1][0] == "0"
            ):

                gain = runs[i - 1][1] + runs[i + 1][1]

                ans = max(ans, original + gain)

        return ans