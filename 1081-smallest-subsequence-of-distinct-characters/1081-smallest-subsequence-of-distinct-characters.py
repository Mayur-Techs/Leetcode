class Solution:
    def smallestSubsequence(self, s: str) -> str:

        # Last index where each character appears
        last = {}

        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        seen = set()

        for i, ch in enumerate(s):

            # Already included
            if ch in seen:
                continue

            # Remove larger characters if they appear later
            while (
                stack
                and ch < stack[-1]
                and last[stack[-1]] > i
            ):
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)