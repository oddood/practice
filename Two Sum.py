"""
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not
use the same element twice.
You can return the answer in any order.
"""


class TwoSum:
    def solution(self, nums, target):
        list_len = len(nums)
        for i in range(list_len - 1):
            for j in range(i + 1, list_len):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def test(self):
        successes = 0
        tests = 1
        answer = self.solution([2, 7, 11, 15], 9)
        if answer[0] == 0 and answer[1] == 1:
            successes += 1

        print("All tests complete.\n{0} correct of {1}; {2}% success rate."
              .format(successes, tests, successes/tests))


two = TwoSum()
two.test()
