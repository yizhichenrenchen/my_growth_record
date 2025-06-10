"""给你一个字符串数组 words ，请你找出所有在 words 的每个字符串中都出现的共用字符（包括重复字符），并以数组形式返回。你可以按 任意顺序 返回答案。


示例 1：

输入：words = ["bella","label","roller"]
输出：["e","l","l"]
示例 2：

输入：words = ["cool","lock","cook"]
输出：["c","o"]"""
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        min_freq = [0] * 26
        for char in words[0]:
            min_freq[ord(char) - ord('a')] += 1

        for word in words[1:]:
            freq = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                freq[idx] += 1

            for i in range(26):
                if freq[i] < min_freq[i]:
                    min_freq[i] = freq[i]

        result = []
        for i in range(26):
            if min_freq[i] > 0:
                char = chr(ord('a') + i)
                result.extend([char] * min_freq[i])

        return result

m = Solution()
print(m.commonChars(["bella","label","roller"]))

