import unittest
import game
import image
import numpy as np

class Tests(unittest.TestCase):
    # Sample tests from python docs
    # KEEP FOR REFERENCE
    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)
    
    def test_pad(self):
        # this test might be redundant since it's really only testing
        # whether or not I know how to use a match-case and my ability
        # to call a library function lol
        pass

    def test_neighbors(self):
        def run_test(grid, expected):
            pt = (1, 1)
            actual = game.count_neighbors(grid, pt[0], pt[1])
            self.assertEqual(actual, expected)

        # dead cell no neighbors
        grid = np.zeros((3, 3), int)
        run_test(grid, 0)

        # no neighbors, confirms that current cell is not counted
        grid = np.array([[0,0,0],
                         [0,1,0],
                         [0,0,0]], int)
        run_test(grid, 0)

        # all neighbors, should confirm that all valid positions are counted
        grid = np.array([[1,1,1],
                         [1,0,1],
                         [1,1,1]], int)
        run_test(grid, 8)


    def test_nextgen(self):
        pass

    def test_rungame(self):
        pass

    def test_normalize(self):
        pass

    def test_denormalize(self):
        pass

    def test_open(self):
        pass

    def test_apply(self):
        pass


if __name__ == '__main__':
    unittest.main()