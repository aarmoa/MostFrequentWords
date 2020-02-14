from MostFrequentWords import Solution
import unittest

class SolutionTest(unittest.TestCase):

    def test_twoTopFrequentWords(self):
        words = ['daily', 'interview', 'pro', 'pro', 'for', 'daily', 'pro', 'problems']
        self.assertEquals(Solution().topKFrequent(words, 2), ['pro', 'daily'])

if __name__ == '__main__':
    unittest.main()