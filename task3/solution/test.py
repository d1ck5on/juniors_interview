import unittest
from solution import appearance


class CheckAppearance(unittest.TestCase):
    def test_base(self):
        test = {'intervals': {'lesson': [1594663200, 1594666800],
                              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
                              },
                'answer': 3117
                }
        test_answer = appearance(test['intervals'])
        self.assertEqual(test_answer, test['answer'])

    def test_intersecting_intervals(self):
        test = {'intervals': {'lesson': [2800, 6400],
                              'pupil': [2789, 4500, 2807, 4542, 4512, 4513, 4564, 5150, 4581, 4582, 4734, 5009, 5095, 5096, 5106, 6480, 5158, 5773, 5849, 6480, 6500, 6875, 6502, 6503, 6524, 6524, 6579, 6641],
                              'tutor': [35, 364, 2749, 5148, 5149, 6463]},
                'answer': 3577
                }
        test_answer = appearance(test['intervals'])
        self.assertEqual(test_answer, test['answer'])

    def test_out_of_bounds(self):
        test = {'intervals': {'lesson': [1594692000, 1594695600],
                              'pupil': [1594692033, 1594696347],
                              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
                              },
                'answer': 3565
                }
        test_answer = appearance(test['intervals'])
        self.assertEqual(test_answer, test['answer'])

    def test_no_intersection(self):
        test = {'intervals': {'lesson': [0, 10],
                              'pupil': [12, 15],
                              'tutor': [3, 5, 7, 11]
                              },
                'answer': 0
                }
        test_answer = appearance(test['intervals'])
        self.assertEqual(test_answer, test['answer'])

    def test_empty_intervals(self):
        test = {'intervals': {'lesson': [],
                              'pupil': [],
                              'tutor': []
                              },
                'answer': 0
                }
        test_answer = appearance(test['intervals'])
        self.assertEqual(test_answer, test['answer'])


if __name__ == "__main__":
    unittest.main()
