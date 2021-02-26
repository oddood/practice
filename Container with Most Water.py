"""
Given n non-negative integers a1, a2, ..., aN, where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
the line i is at (i, ai) and (i, 0). Find two lines, which, together with the
x-axis forms a container such that the container contains the most water.
"""


class ContainerWithMostWater:
    def solution(self, height):
        options = len(height)
        if options < 2:
            return -1

        max_volume = 0

        for i in range(options):
            for j in range(i+1, options):
                best = min(height[i], height[j])
                volume = best*(j-i)
                if volume > max_volume:
                    max_volume = volume

        return max_volume

    def test(self):
        successes = 0
        tests = 3

        ans = self.solution([1, 2, 1])
        if ans == 2:
            successes += 1
        else:
            print("Test 1 failed. Expected 2, found " + str(ans))

        ans = self.solution([4, 3, 2, 1, 4])
        if ans == 16:
            successes += 1
        else:
            print("Test 2 failed. Expected 16, found " + str(ans))

        ans = self.solution([1, 8, 6, 2, 5, 4, 8, 3, 7])
        if ans == 49:
            successes += 1
        else:
            print("Test 3 failed. Expected 49, found " +str(ans))

        print("All tests complete.\n{0} correct of {1}; {2}% success rate."
              .format(successes, tests, (successes / tests)*100))


this = ContainerWithMostWater()
this.test()
