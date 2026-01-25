import unittest
from gen_bin_tree2 import gen_bin_tree2



class GenBinTreeTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            gen_bin_tree2(0, 18,
                          lambda x: (x-8)*3, lambda x: (x+8)*2),
                   {'18': []}
                         )


    def test_2(self):
        self.assertEqual(
            gen_bin_tree2(2, 18,
                         lambda x: (x-8)*3, lambda x: (x+8)*2),
                  {'18': [{'30': [{'66': []}, {'76': []}]},
                         {'52': [{'132': []}, {'120': []}]}]}
                        )

    def test_3(self):
        self.assertEqual(
            gen_bin_tree2(3, 18,
                          lambda x: (x - 8) * 3, lambda x: (x + 8) * 2),
                   {'18': [{'30': [{'66': [{'174': []}, {'148': []}]},
                          {'76': [{'204': []}, {'168': []}]}]},
                          {'52': [{'132': [{'372': []}, {'280': []}]},
                          {'120': [{'336': []}, {'256': []}]}]}]}
        )
