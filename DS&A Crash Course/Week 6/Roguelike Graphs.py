from __future__ import annotations
import unittest


# =============== BEGIN DO NOT MODIFY ========================
class Treasure:
    pass


class Monster:
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage
        self.next = []

    def append_monster(self, monster: Monster):
        self.next.append(monster)

    def append_treasure(self, treasure: Treasure):
        self.next.append(treasure)


class Player:
    def __init__(self, health: int):
        self.health = health

    def battle(self, monster: Monster):
        self.health -= monster.damage


# =============== END DO NOT MODIFY ========================

class Dungeon:
    def __init__(self, monster: Monster):
        self.monster = monster

        # Is it possible for player to make it to the end if they start with infinite health?

    def can_at_least_one_path_make_it(self) -> bool:
        # does path exist
        from collections import deque  # using deque for deque practice

        queue = deque([self.monster])

        # bfs
        while queue:
            next_node = queue.popleft()
            if type(next_node) is Treasure:
                return True
            children = next_node.next
            for child in children:
                queue.append(child)

        return False

    # Is it possible for player to make it to end without losing all their health?
    # O(E * log E) ?
    def can_make_it(self, player: Player) -> bool:
        # does path exist at cost < health

        # find shortest path
        # form path, tracking distance (damage)
        # compare total distance (damage) to health (boundary)

        import heapq
        import time  # heapq oof

        heap = [(self.monster.damage, time.time(), self.monster, None)]
        dmg = dict()  # also visited

        # find shortest path
        while heap:
            node = heapq.heappop(heap)
            current = node[2]
            dmg[current] = node[0]
            if type(current) is Treasure:
                if player.health >= dmg[current]:
                    return True
                return False

            children = current.next
            for child in children:
                if child in dmg:
                    continue
                damage = node[0]
                if type(child) is not Treasure:
                    damage += child.damage
                heapq.heappush(heap, (damage, time.time(), child, current))

        return False

    # Will any path make it to the end? Can they choose randomly and always make it?
    def can_all_paths_make_it(self, player: Player) -> bool:
        # does a path fail
        # find failure

        # find longest path
        # copy/paste
        import heapq
        import time  # heapq oof

        heap = [(-self.monster.damage, time.perf_counter(), self.monster, None)]
        dmg = dict()  # also visited

        # find longest path
        while heap:
            node = heapq.heappop(heap)
            current = node[2]
            dmg[current] = node[0]
            if type(current) is Treasure:
                if player.health >= -dmg[current]:
                    return True
                return False

            children = current.next
            # terminal nodes
            if len(children) < 1:
                return False

            for child in children:
                # if child in dmg:
                #     continue
                damage = node[0]
                if type(child) is not Treasure:
                    damage -= child.damage
                print((damage, time.time_ns(), child, current))
                heapq.heappush(heap, (damage, time.perf_counter(), child, current))

        return False

    # If picking paths randomly, what is the probability player will make it to the end?
    def probability_player_will_make_it(self, player: Player) -> float:
        # each path assigned a probability
        # successful paths summed

        success = 0
        stack = [[player.health - self.monster.damage, 1.0, self.monster]]
        # no visited exclusion

        while stack:
            current = stack.pop()
            # if hp fail or no children
            if current[0] < 0 or len(current[-1].next) < 1:
                continue

            for child in current[-1].next:
                if child in current:  # undirected graph loops
                    continue
                if type(child) is Treasure:
                    success += current[1]
                    continue
                extended = current[:]
                extended.append(child)
                extended[0] -= child.damage
                extended[1] *= 1 / len(current[-1].next)
                stack.append(extended)

        return success


class GraphTest(unittest.TestCase):

    # a(3) -> b(4) -> c(5) -> treasure
    def create_dungeon(self) -> Dungeon:
        a = Monster("a", 3)
        b = Monster("b", 4)
        c = Monster("c", 5)
        treasure = Treasure()
        a.append_monster(b)
        b.append_monster(c)
        c.append_treasure(treasure)

        return Dungeon(a)

    # a(3) -> b(4)  c(5) -> treasure
    def create_dungeon2(self) -> Dungeon:
        a = Monster("a", 3)
        b = Monster("b", 4)
        c = Monster("c", 5)
        treasure = Treasure()
        a.append_monster(b)
        c.append_treasure(treasure)

        return Dungeon(a)

    # a(1) -> b(4)
    #   |      |
    #   v      v
    # c(2) -> d(1) -> treasure
    def create_dungeon3(self):
        a = Monster("a", 1)
        b = Monster("b", 4)
        c = Monster("c", 2)
        d = Monster("d", 1)
        treasure = Treasure()
        a.append_monster(b)
        a.append_monster(c)
        b.append_monster(d)
        c.append_monster(d)
        d.append_treasure(treasure)

        return Dungeon(a)

    # a(1) -> b(4) -> e(1)
    #   |      |
    #   v      v
    # c(2) -> d(1) -> treasure

    '''
    Probability review: Just because there are 2 different possiblilites does not 
    mean that they are equal probability. For example, on any given day, there could be 
    rain or no rain. That doesn't imply that rain has a 50% chance.

    In this case, there are 3 different paths:
    a->c->d->treasure, a->b->d->treasure, and a->b->e. 

    Here, a->c->d->tresure has a 50% chance of happening, a->b->e is 25%, and a->b->d->treasure is 25%. 
    An easy way to think about it that the probability of A reaching C is 50% and C reaching D is 100%
    and D reaching Treasure is 100%. Overall, it would be 50% chance to do A->C->D->Treasure.
    '''

    def create_dungeon4(self):
        a = Monster("a", 1)
        b = Monster("b", 4)
        c = Monster("c", 2)
        d = Monster("d", 1)
        e = Monster("e", 1)
        treasure = Treasure()
        a.append_monster(b)
        a.append_monster(c)
        b.append_monster(d)
        c.append_monster(d)
        b.append_monster(e)
        d.append_treasure(treasure)

        return Dungeon(a)

    # a(1) -> b(5) -> e(1)
    #   |      |       |
    #   v      v       v
    # c(2) -> d(7) -> f(2) -> treasure
    # optimal -> a -> b -> e -> f
    def create_dungeon5(self):
        a = Monster("a", 1)
        b = Monster("b", 5)
        c = Monster("c", 2)
        d = Monster("d", 7)
        e = Monster("e", 1)
        f = Monster("f", 2)
        treasure = Treasure()
        a.append_monster(b)
        a.append_monster(c)
        b.append_monster(e)
        b.append_monster(d)
        c.append_monster(d)
        d.append_monster(f)
        e.append_monster(f)
        f.append_treasure(treasure)

        return Dungeon(a)

    # a(1) -> b(5) -> e(1) ------
    #   |      |       |        |
    #   v      v       v        v
    # c(2) -> d(7) -> f(2) -> treasure
    # optimal -> a -> b -> e -> f
    def create_dungeon6(self):
        a = Monster("a", 1)
        b = Monster("b", 5)
        c = Monster("c", 2)
        d = Monster("d", 7)
        e = Monster("e", 1)
        f = Monster("f", 2)
        treasure = Treasure()
        a.append_monster(b)
        a.append_monster(c)
        b.append_monster(e)
        b.append_monster(d)
        c.append_monster(d)
        d.append_monster(f)
        e.append_monster(f)
        e.append_treasure(treasure)
        f.append_treasure(treasure)

        return Dungeon(a)

    def test_can_at_least_one_path_make_it(self):
        dungeon = self.create_dungeon()
        self.assertEqual(dungeon.can_at_least_one_path_make_it(), True)

        dungeon = self.create_dungeon2()
        self.assertEqual(dungeon.can_at_least_one_path_make_it(), False)

    def test_can_all_paths_make_it(self):
        dungeon = self.create_dungeon()
        self.assertEqual(dungeon.can_all_paths_make_it(Player(11)), False)

        dungeon = self.create_dungeon()
        self.assertEqual(dungeon.can_all_paths_make_it(Player(12)), True)

        dungeon = self.create_dungeon2()
        self.assertEqual(dungeon.can_all_paths_make_it(Player(7)), False)

        dungeon = self.create_dungeon3()
        self.assertEqual(dungeon.can_all_paths_make_it(Player(5)), False)

        dungeon = self.create_dungeon3()
        self.assertEqual(dungeon.can_all_paths_make_it(Player(6)), True)

        dungeon = self.create_dungeon4()
        self.assertEqual(dungeon.can_all_paths_make_it(Player(100)), False)

    def test_probability_player_will_make_it(self):
        dungeon = self.create_dungeon()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(12)), 1.0)

        dungeon = self.create_dungeon()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(11)), 0.0)

        dungeon = self.create_dungeon2()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(100)), 0.0)

        dungeon = self.create_dungeon3()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(1)), 0.0)

        dungeon = self.create_dungeon3()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(5)), 0.5)

        dungeon = self.create_dungeon3()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(100)), 1.0)

        dungeon = self.create_dungeon4()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(1)), 0.0)

        dungeon = self.create_dungeon4()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(5)), 0.5)

        dungeon = self.create_dungeon4()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(100)), 0.75)

    def test_can_make_it(self):
        dungeon = self.create_dungeon5()
        self.assertEqual(dungeon.can_make_it(Player(9)), True)

        dungeon = self.create_dungeon5()
        self.assertEqual(dungeon.can_make_it(Player(8)), False)

        dungeon = self.create_dungeon6()
        self.assertEqual(dungeon.can_make_it(Player(7)), True)

        dungeon = self.create_dungeon6()
        self.assertEqual(dungeon.can_make_it(Player(6)), False)