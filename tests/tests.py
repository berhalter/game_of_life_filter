import unittest
import sys
sys.path.append("..") #this is needed in order to import gol and filter since they are not in the current directory

import gol
import filter
import numpy as np


class Tests(unittest.TestCase):
    pad_mode = "dead" #test with different modes?

    """Tests for count_neighbors()"""
    def test_neghbors_dead(self):
        # dead cell no neighbors
        grid = np.zeros((3, 3), int)
        actual = gol.count_neighbors(grid, 1, 1)
        self.assertEqual(actual, 0)

    def test_neghbors_live(self):
        # no neighbors, confirms that current cell is not counted
        grid = np.array([[0,0,0],
                         [0,1,0],
                         [0,0,0]], int)
        actual = gol.count_neighbors(grid, 1, 1)
        self.assertEqual(actual, 0)

    def test_neghbors_all(self):
        # all neighbors, should confirm that all valid positions are counted
        grid = np.array([[1,1,1],
                         [1,0,1],
                         [1,1,1]], int)
        actual = gol.count_neighbors(grid, 1, 1)
        self.assertEqual(actual, 8)

    """Tests for compute_next_gen()"""
    def test_nextgen_all_0(self):
        # grid of all zeroes
        grid = np.zeros((3,3), int)
        grid = np.pad(grid, 1, mode="constant", constant_values=0)
        expected = np.zeros((3,3), int)
        expected = np.pad(expected, 1, mode="constant", constant_values=0)
        actual = gol.compute_next_gen(grid, self.pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

    def test_nextgen_all_1(self):
        # grid of all ones
        grid = np.ones((3,3), int)
        grid = np.pad(grid, 1, mode="constant", constant_values=0)
        expected = np.array([[1,0,1],
                             [0,0,0],
                             [1,0,1]], int)
        expected = np.pad(expected, 1, mode="constant", constant_values=0)
        actual = gol.compute_next_gen(grid, self.pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

    def test_nextgen_live_1(self):
        # "any live cell with fewer than two live neighbors dies"
        grid = np.array([[0,1,0],
                         [0,1,0],
                         [0,0,0]], int)
        grid = np.pad(grid, 1, mode="constant", constant_values=0)
        expected = np.zeros((3,3), int)
        expected = np.pad(expected, 1, mode="constant", constant_values=0)
        actual = gol.compute_next_gen(grid, self.pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

    def test_nextgen_live_2(self):    
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

    def test_nextgen_live_3(self):
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

    def test_nextgen_live_4(self):
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

    def test_nextgen_dead_3(self):
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
        
    """Tests for run_game()"""
    def test_rungame_block_1(self):
        #test block 1 generation
        fblock = "./inputs/block.txt"
        grid = np.loadtxt(fblock, dtype=int)
        expected = np.loadtxt(fblock, dtype=int)
        actual = gol.run_game(grid, 1, self.pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

    def test_rungame_blinker_0(self):
        #test blinker 0 generations
        fblinker0 = "./inputs/blinker0.txt"
        grid = np.loadtxt(fblinker0, dtype=int)
        expected = np.loadtxt(fblinker0, dtype=int)
        actual = gol.run_game(grid, 0, self.pad_mode)
        self.assertTrue(np.array_equal(actual, expected))
    
    def test_rungame_blinker_1(self):
        #test blinker 1 generation
        fblinker0 = "./inputs/blinker0.txt"
        fblinker1 = "./inputs/blinker1.txt"
        grid = np.loadtxt(fblinker0, dtype=int)
        expected = np.loadtxt(fblinker1, dtype=int)
        actual = gol.run_game(grid, 1, self.pad_mode)
        self.assertTrue(np.array_equal(actual, expected))
        
    def test_rungame_blinker_2(self):
        #test blinker 2 generations
        fblinker0 = "./inputs/blinker0.txt"
        fblinker2 = fblinker0 #blinker has a 2 generation cycle
        grid = np.loadtxt(fblinker0, dtype=int)
        expected = np.loadtxt(fblinker2, dtype=int)
        actual = gol.run_game(grid, 2, self.pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

    def test_rungame_cross_1(self):
        #test cross 1 generation
        fcross0 = "./inputs/cross0.txt"
        fcross1 = "./inputs/cross1.txt"
        grid = np.loadtxt(fcross0, dtype=int)
        expected = np.loadtxt(fcross1, dtype=int)
        actual = gol.run_game(grid, 1, self.pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

    def test_rungame_cross_2(self):
        #test cross 2 generations
        fcross0 = "./inputs/cross0.txt"
        fcross2 = "./inputs/cross2.txt"
        grid = np.loadtxt(fcross0, dtype=int)
        expected = np.loadtxt(fcross2, dtype=int)
        actual = gol.run_game(grid, 2, self.pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

    def test_rungame_cross_3(self):
        #test cross 3 generations
        fcross0 = "./inputs/cross0.txt"
        fcross3 = fcross0 #cross has a 3 generation cycle
        grid = np.loadtxt(fcross0, dtype=int)
        expected = np.loadtxt(fcross3, dtype=int)
        actual = gol.run_game(grid, 3, self.pad_mode)
        self.assertTrue(np.array_equal(actual, expected))

    """Tests for normalize()"""
    def test_normalize_dead(self):
        # all dead
        grid = np.zeros((3,3), int)
        expected = grid
        actual = filter.normalize(grid)
        self.assertTrue(np.array_equal(actual, expected))
    
    def test_normalize_live(self):
        # all live
        grid = np.full((3,3), 255, int)
        expected = np.ones((3,3), int)
        actual = filter.normalize(grid)
        self.assertTrue(np.array_equal(actual, expected))

    """Tests for denormalize()"""
    def test_denormalize_dead(self):
        # all dead
        grid = np.zeros((3,3), int)
        expected = grid
        actual = filter.denormalize(grid)
        self.assertTrue(np.array_equal(actual, expected))
    
    def test_denormalize_live(self):
        # all live
        grid = np.ones((3,3), int)
        expected = np.full((3,3), 255, int)
        actual = filter.denormalize(grid)
        self.assertTrue(np.array_equal(actual, expected))



if __name__ == '__main__':
    unittest.main()