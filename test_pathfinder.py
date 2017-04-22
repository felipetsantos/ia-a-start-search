#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import unittest
from common import *
from pathfinder import *

# Map definitions
TRIVIAL = "trivial.txt"
TRIVIAL_SOLUTION = []
TRIVIAL_MAX_TREE_HEIGHT = 0
TRIVIAL_GRADE = 0.25

EASY = "easy.txt"
EASY_SOLUTION = [
    MOVE_UP, MOVE_UP, MOVE_UP, MOVE_UP, MOVE_UP, MOVE_UP,
    MOVE_RIGHT, MOVE_RIGHT, MOVE_RIGHT]
EASY_MAX_TREE_HEIGHT = 9
EASY_GRADE = 0.25

MEDIUM = "medium.txt"
MEDIUM_SOLUTION = [
    MOVE_DOWN, MOVE_DOWN, MOVE_DOWN, MOVE_DOWN, MOVE_DOWN, MOVE_DOWN, MOVE_DOWN,
    MOVE_RIGHT, MOVE_RIGHT, MOVE_RIGHT, MOVE_RIGHT, MOVE_RIGHT,
    MOVE_UP, MOVE_UP, MOVE_UP,
    MOVE_RIGHT, MOVE_RIGHT, MOVE_RIGHT,
    MOVE_UP, MOVE_UP,
    MOVE_LEFT, MOVE_LEFT, MOVE_LEFT,
    MOVE_UP, MOVE_UP,
    MOVE_LEFT, MOVE_LEFT, MOVE_LEFT]
MEDIUM_MAX_TREE_HEIGHT = 28
MEDIUM_GRADE = 0.25

UNSOLVABLE = "unsolvable.txt"
UNSOLVABLE_SOLUTION = None
UNSOLVABLE_MAX_TREE_HEIGHT = None
UNSOLVABLE_GRADE = 0.25

HARD = "hard.txt"
HARD_SOLUTION = None
HARD_MAX_TREE_HEIGHT = 998
HARD_GRADE = 0.25
# ==========================================
# Test A*
# ==========================================

class Test_A_Star(unittest.TestCase):

    # ------------------------------------------
    # Setup
    # ------------------------------------------

    @classmethod
    def setUpClass(cls):
        cls.grade = 0.0
        cls.total = 0.0

    @classmethod
    def tearDownClass(cls):
        print "  Grade: ", cls.grade, " of ", cls.total

    # ------------------------------------------
    # Common tests
    # ------------------------------------------

    def solvable(self, map_name, expected):
        map = read_map(map_name)
        pathfinder = PathFinder_A_Star()
        pathfinder.solve(map)
        self.assertEqual(pathfinder.get_solvable(map), expected)

    def plan_match(self, map_name, moves):
        map = read_map(map_name)
        plan = PathFinder_A_Star().solve(map)
        self.assertEqual(plan, moves)

    def max_tree_height(self, map_name, height):
        map = read_map(map_name)
        pathfinder = PathFinder_A_Star()
        plan = pathfinder.solve(map)
        self.assertEqual(pathfinder.get_max_tree_height(map), height)

    def min_moves(self, map_name, moves):
        map = read_map(map_name)
        pathfinder = PathFinder_A_Star()
        plan = pathfinder.solve(map)
        if moves != None:
            self.assertEqual(pathfinder.get_min_moves(map), len(moves))
        else:
            self.assertEqual(pathfinder.get_min_moves(map), moves)

    # =============
    # = Heuristic =
    # =============
    
    def test_heuristic(self):
        pathfinder = PathFinder_A_Star()
        p1 = Point(1, 2)
        p2 = Point(1, 3)
        self.assertEqual(pathfinder.heuristic(p1, p2),1)
        p1 = Point(2, 2)
        p2 = Point(1, 3)
        self.assertEqual(pathfinder.heuristic(p1, p2),2)
        p1 = Point(20, 2)
        p2 = Point(1, 2)
        self.assertEqual(pathfinder.heuristic(p1, p2),19)

    # ------------------------------------------
    # Trivial
    # ------------------------------------------

    def test_trivial_solvable(self):
        self.__class__.total += TRIVIAL_GRADE
        self.solvable(TRIVIAL, True)
        self.__class__.grade += TRIVIAL_GRADE

    def test_trivial_plan_match(self):
        self.__class__.total += TRIVIAL_GRADE
        self.plan_match(TRIVIAL, TRIVIAL_SOLUTION)
        self.__class__.grade += TRIVIAL_GRADE

    def test_trivial_max_tree_height(self):
        self.__class__.total += TRIVIAL_GRADE
        self.max_tree_height(TRIVIAL, TRIVIAL_MAX_TREE_HEIGHT)
        self.__class__.grade += TRIVIAL_GRADE

    def test_trivial_min_moves(self):
        self.__class__.total += TRIVIAL_GRADE
        self.min_moves(TRIVIAL, TRIVIAL_SOLUTION)
        self.__class__.grade += TRIVIAL_GRADE

    # ------------------------------------------
    # Easy
    # ------------------------------------------

    def test_easy_solvable(self):
        self.__class__.total += EASY_GRADE
        self.solvable(EASY, True)
        self.__class__.grade += EASY_GRADE

    def test_easy_plan_match(self):
        self.__class__.total += EASY_GRADE
        self.plan_match(EASY, EASY_SOLUTION)
        self.__class__.grade += EASY_GRADE

    def test_easy_max_tree_height(self):
        self.__class__.total += EASY_GRADE
        self.max_tree_height(EASY, EASY_MAX_TREE_HEIGHT)
        self.__class__.grade += EASY_GRADE

    def test_easy_min_moves(self):
        self.__class__.total += EASY_GRADE
        self.min_moves(EASY, EASY_SOLUTION)
        self.__class__.grade += EASY_GRADE

    # ------------------------------------------
    # Medium
    # ------------------------------------------

    def test_medium_solvable(self):
        self.__class__.total += MEDIUM_GRADE
        self.solvable(MEDIUM, True)
        self.__class__.grade += MEDIUM_GRADE

    def test_medium_plan_match(self):
        self.__class__.total += MEDIUM_GRADE
        self.plan_match(MEDIUM, MEDIUM_SOLUTION)
        self.__class__.grade += MEDIUM_GRADE

    def test_medium_max_tree_height(self):
        self.__class__.total += MEDIUM_GRADE
        self.max_tree_height(MEDIUM, MEDIUM_MAX_TREE_HEIGHT)
        self.__class__.grade += MEDIUM_GRADE

    def test_medium_min_moves(self):
        self.__class__.total += MEDIUM_GRADE
        self.min_moves(MEDIUM, MEDIUM_SOLUTION)
        self.__class__.grade += MEDIUM_GRADE

    # ------------------------------------------
    # Unsolvable
    # ------------------------------------------

    def test_unsolvable_solvable(self):
        self.__class__.total += UNSOLVABLE_GRADE
        self.solvable(UNSOLVABLE, False)
        self.__class__.grade += UNSOLVABLE_GRADE

    def test_unsolvable_plan_match(self):
        self.__class__.total += UNSOLVABLE_GRADE
        self.plan_match(UNSOLVABLE, UNSOLVABLE_SOLUTION)
        self.__class__.grade += UNSOLVABLE_GRADE

    def test_unsolvable_max_tree_height(self):
        self.__class__.total += UNSOLVABLE_GRADE
        self.max_tree_height(UNSOLVABLE, UNSOLVABLE_MAX_TREE_HEIGHT)
        self.__class__.grade += UNSOLVABLE_GRADE

    def test_unsolvable_min_moves(self):
        self.__class__.total += UNSOLVABLE_GRADE
        self.min_moves(UNSOLVABLE, UNSOLVABLE_SOLUTION)
        self.__class__.grade += UNSOLVABLE_GRADE


    # ------------------------------------------
    # Hard
    # ------------------------------------------

    def test_hard_solvable(self):
        self.__class__.total += HARD_GRADE
        self.solvable(HARD, True)
        self.__class__.grade += HARD_GRADE

    def get_hard_moves(self):
        actions = []
        for i in range(1,500):
            actions.append(MOVE_RIGHT)
        for i in range(1,500):
            actions.append(MOVE_DOWN) 
        return actions

    def test_hard_plan_match(self):
        self.__class__.total += HARD_GRADE
        actions = self.get_hard_moves()
        self.plan_match(HARD, actions)
        self.__class__.grade += HARD_GRADE

    def test_hard_max_tree_height(self):
        self.__class__.total += HARD_GRADE
        self.max_tree_height(HARD, HARD_MAX_TREE_HEIGHT)
        self.__class__.grade += HARD_GRADE

    def test_unsolvable_min_moves(self):
        self.__class__.total += HARD_GRADE
        actions = self.get_hard_moves()
        self.min_moves(HARD, actions)
        self.__class__.grade += HARD_GRADE

if __name__ == '__main__':
    unittest.main()
