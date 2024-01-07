from typing import List


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # find topological sort
        topo = list()

        # initialize in/out degree stores
        in_deg = [0] * numCourses
        out_deg = {i: [] for i in range(numCourses)}

        # find in/out degrees
        for pre_req in prerequisites:
            child = pre_req[0]
            parent = pre_req[1]
            in_deg[child] += 1
            out_deg[parent].append(child)

        # seed agenda with zero in-degrees
        agenda = list()  # could also use queue
        for i in range(len(in_deg)):
            if in_deg[i] == 0:
                agenda.append(i)

        # consume agenda by decrementing children's incoming
        # degrees, and adding zero in-degrees to agenda
        while agenda:
            next_ = agenda.pop()
            topo.append(next_)
            for child in out_deg[next_]:
                in_deg[child] -= 1
                if in_deg[child] == 0:
                    agenda.append(child)

        # return True iff every element was 
        # able to be topologically sorted
        if len(topo) == numCourses:
            return True
        return False
