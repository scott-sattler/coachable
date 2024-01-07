# from collections import deque

# agenda.popleft()
# agenda.appendleft()


# we're looking for a valid path
# cycle detection, given uniqueness
# assumes every course can be seen at least once within prerequisites

# successor <- predecessor

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # find topological sort
        topo = list()

        # find in/out degrees
        in_deg = dict()
        out_deg = dict()
        for course in prerequisites:
            # increment in-degrees of node course[0]
            if course[0] not in in_deg:
                in_deg[course[0]] = 0
            in_deg[course[0]] += 1
            # append course[0] (successor) of course[1] (predecessor) out-degree
            if course[1] not in out_deg:
                out_deg[course[1]] = []
            out_deg[course[1]].append(course[0])
            # # turn out-degree into adjacency list
            # if course[0] not in out_deg:
            #     out_deg[course[0]] = []
            # if course[1] not in in_deg:
            #     in_deg[course[1]] = 0
            for i in range(numCourses):
                if i not in in_deg:
                    in_deg[i] = 0

        # add zero in-degrees to stack (or queue)
        agenda = list()
        for course in in_deg:
            if in_deg[course] == 0:
                agenda.append(course)

        # process zero in-degrees until agenda is consumed
        while agenda:
            next_course = agenda.pop()
            topo.append(next_course)
            if next_course not in out_deg:
                continue
            for child in out_deg[next_course]:
                in_deg[child] -= 1
                if in_deg[child] == 0:
                    agenda.append(child)

        return True if len(topo) == len(in_deg) else False
