import unittest
import gol
import filter
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
            actual = gol.count_neighbors(grid, pt[0], pt[1])
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
        print()
        pad_mode = "dead"
        # grid of all zeroes
        grid = np.zeros((3,3), int)
        grid = np.pad(grid, 1, mode="constant", constant_values=0)
        expected = np.zeros((3,3), int)
        expected = np.pad(expected, 1, mode="constant", constant_values=0)
        actual = gol.compute_next_gen(grid, pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

        # grid of all ones
        grid = np.ones((3,3), int)
        grid = np.pad(grid, 1, mode="constant", constant_values=0)
        expected = np.array([[1,0,1],
                             [0,0,0],
                             [1,0,1]], int)
        expected = np.pad(expected, 1, mode="constant", constant_values=0)
        actual = gol.compute_next_gen(grid, pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

        # "any live cell with fewer than two live neighbors dies"
        grid = np.array([[0,1,0],
                         [0,1,0],
                         [0,0,0]], int)
        grid = np.pad(grid, 1, mode="constant", constant_values=0)
        expected = np.zeros((3,3), int)
        expected = np.pad(expected, 1, mode="constant", constant_values=0)
        actual = gol.compute_next_gen(grid, pad_mode)
        self.assertTrue(np.array_equal(actual, expected))
        
        # "any live cell with two or three live neighbors lives on to the next generation"
        grid = np.array([[0,0,0],
                         [1,1,1],
                         [0,0,0]], int)
        grid = np.pad(grid, 1, mode="constant", constant_values=0)
        expected = np.array([[0,1,0],
                             [0,1,0],
                             [0,1,0]], int)
        expected = np.pad(expected, 1, mode="constant", constant_values=0)
        actual = gol.compute_next_gen(grid, pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

        grid = np.array([[0,1,0],
                         [0,1,0],
                         [1,0,1]], int)
        grid = np.pad(grid, 1, mode="constant", constant_values=0)
        expected = np.array([[0,0,0],
                             [1,1,1],
                             [0,1,0]], int)
        expected = np.pad(expected, 1, mode="constant", constant_values=0)
        actual = gol.compute_next_gen(grid, pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

        # "any live cell with more than three live neighbors dies, as if by overpopulation"
        grid = np.array([[1,0,1],
                         [0,1,0],
                         [1,0,1]], int)
        grid = np.pad(grid, 1, mode="constant", constant_values=0)
        expected = np.array([[0,1,0],
                             [1,0,1],
                             [0,1,0]], int)
        expected = np.pad(expected, 1, mode="constant", constant_values=0)
        actual = gol.compute_next_gen(grid, pad_mode)
        self.assertTrue(np.array_equal(actual, expected))
        
        # "any dead cell with exactly three live neighbors becomes a live cell"
        grid = np.array([[0,1,0],
                         [0,0,0],
                         [1,0,1]], int)
        grid = np.pad(grid, 1, mode="constant", constant_values=0)
        expected = np.array([[0,0,0],
                             [0,1,0],
                             [0,0,0]], int)
        expected = np.pad(expected, 1, mode="constant", constant_values=0)
        actual = gol.compute_next_gen(grid, pad_mode)
        self.assertTrue(np.array_equal(actual, expected))
        

    def test_rungame(self):
        pad_mode = "dead" #test with different modes!!!
        #test block 1 generation
        grid = np.array([[0,0,0,0],
                         [0,1,1,0],
                         [0,1,1,0],
                         [0,0,0,0]], int)
        expected = np.array([[0,0,0,0],
                             [0,1,1,0],
                             [0,1,1,0],
                             [0,0,0,0]], int)
        actual = gol.run_game(grid, 1, pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

        #test blinker 1 generation
        grid = np.array([[0,0,0,0,0],
                         [0,0,1,0,0],
                         [0,0,1,0,0],
                         [0,0,1,0,0],
                         [0,0,0,0,0]], int)
        expected = np.array([[0,0,0,0,0],
                             [0,0,0,0,0],
                             [0,1,1,1,0],
                             [0,0,0,0,0],
                             [0,0,0,0,0]], int)
        actual = gol.run_game(grid, 1, pad_mode)
        self.assertTrue(np.array_equal(actual, expected))
        #test blinker 2 generations
        expected = np.array([[0,0,0,0,0],
                             [0,0,1,0,0],
                             [0,0,1,0,0],
                             [0,0,1,0,0],
                             [0,0,0,0,0]], int)
        actual = gol.run_game(grid, 2, pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

        #test pulsar 1 generation
        #test pulsar 2 generations
        #test pulsar 3 generations

        pass

    def test_normalize(self):
        # all dead
        grid = np.zeros((3,3), int)
        expected = grid
        actual = filter.normalize(grid)
        self.assertTrue(np.array_equal(actual, expected))

        # all live
        grid = np.array([[255,255,255],
                         [255,255,255],
                         [255,255,255]], int)
        expected = np.ones((3,3), int)
        actual = filter.normalize(grid)
        self.assertTrue(np.array_equal(actual, expected))

    def test_denormalize(self):
        # all dead
        grid = np.zeros((3,3), int)
        expected = grid
        actual = filter.denormalize(grid)
        self.assertTrue(np.array_equal(actual, expected))

        # all live
        grid = np.ones((3,3), int)
        expected = np.array([[255,255,255],
                             [255,255,255],
                             [255,255,255]], int)
        actual = filter.denormalize(grid)
        self.assertTrue(np.array_equal(actual, expected))

    # I have no idea how to test these next two since they return images. 
    # Not overly concerned about it, since failiure of these implies a failure in
    # a library function or a function I wrote, so I might delete them
    # LOL nvm apply_filter is 100% the bug
    def test_open(self):
        pass

    def test_apply(self):
        pass


if __name__ == '__main__':
    unittest.main()