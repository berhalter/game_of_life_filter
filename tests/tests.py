import unittest
import sys
sys.path.append("..") #this is needed in order to import gol and filter since they are not in the current directory

import gol
import filter
import numpy as np


class Tests(unittest.TestCase):
    pad_mode = "dead" #test with different modes!!!

    def run_neighbors(self, grid, expected):
        pt = (1, 1)
        actual = gol.count_neighbors(grid, pt[0], pt[1])
        self.assertEqual(actual, expected)

    def test_neghbors_dead(self):
        # dead cell no neighbors
        grid = np.zeros((3, 3), int)
        self.run_neighbors(grid, 0)

    def test_neghbors_live(self):
        # no neighbors, confirms that current cell is not counted
        grid = np.array([[0,0,0],
                         [0,1,0],
                         [0,0,0]], int)
        self.run_neighbors(grid, 0)

    def test_neghbors_all(self):
        # all neighbors, should confirm that all valid positions are counted
        grid = np.array([[1,1,1],
                         [1,0,1],
                         [1,1,1]], int)
        self.run_neighbors(grid, 8)


    def test_nextgen(self):

        # grid of all zeroes
        grid = np.zeros((3,3), int)
        grid = np.pad(grid, 1, mode="constant", constant_values=0)
        expected = np.zeros((3,3), int)
        expected = np.pad(expected, 1, mode="constant", constant_values=0)
        actual = gol.compute_next_gen(grid, self.pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

        # grid of all ones
        grid = np.ones((3,3), int)
        grid = np.pad(grid, 1, mode="constant", constant_values=0)
        expected = np.array([[1,0,1],
                             [0,0,0],
                             [1,0,1]], int)
        expected = np.pad(expected, 1, mode="constant", constant_values=0)
        actual = gol.compute_next_gen(grid, self.pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

        # "any live cell with fewer than two live neighbors dies"
        grid = np.array([[0,1,0],
                         [0,1,0],
                         [0,0,0]], int)
        grid = np.pad(grid, 1, mode="constant", constant_values=0)
        expected = np.zeros((3,3), int)
        expected = np.pad(expected, 1, mode="constant", constant_values=0)
        actual = gol.compute_next_gen(grid, self.pad_mode)
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
        actual = gol.compute_next_gen(grid, self.pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

        grid = np.array([[0,1,0],
                         [0,1,0],
                         [1,0,1]], int)
        grid = np.pad(grid, 1, mode="constant", constant_values=0)
        expected = np.array([[0,0,0],
                             [1,1,1],
                             [0,1,0]], int)
        expected = np.pad(expected, 1, mode="constant", constant_values=0)
        actual = gol.compute_next_gen(grid, self.pad_mode)
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
        actual = gol.compute_next_gen(grid, self.pad_mode)
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
        actual = gol.compute_next_gen(grid, self.pad_mode)
        self.assertTrue(np.array_equal(actual, expected))
        

    def test_rungame(self):
        

        #test block 1 generation
        fblock = "./inputs/block.txt"
        grid = np.loadtxt(fblock, dtype=int)
        expected = np.loadtxt(fblock, dtype=int)
        actual = gol.run_game(grid, 1, self.pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

        #test blinker 1 generation
        fblinker0 = "./inputs/blinker0.txt"
        grid = np.loadtxt(fblinker0, dtype=int)
        expected = np.array([[0,0,0,0,0],
                             [0,0,0,0,0],
                             [0,1,1,1,0],
                             [0,0,0,0,0],
                             [0,0,0,0,0]], int)
        actual = gol.run_game(grid, 1, self.pad_mode)
        self.assertTrue(np.array_equal(actual, expected))
        #test blinker 2 generations
        expected = np.array([[0,0,0,0,0],
                             [0,0,1,0,0],
                             [0,0,1,0,0],
                             [0,0,1,0,0],
                             [0,0,0,0,0]], int)
        actual = gol.run_game(grid, 2, self.pad_mode)
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



if __name__ == '__main__':
    unittest.main()