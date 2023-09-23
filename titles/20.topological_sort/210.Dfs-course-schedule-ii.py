class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] +=1

        todo = []
        for index, count in enumerate(incoming):
            if count ==0:
                todo.append(index)

        top_sort = []
        colors = [0] * numCourses

        for cur_root in todo:
            cycle_found = self.hasCycle(cur_root, colors, graph, top_sort)
            if cycle_found:
                return []
        top_sort.reverse()
        if len(top_sort ) != numCourses : return []
        return top_sort
    def hasCycle(self, cur_node, colors, graph, top_sort):
        # no cycle
        if colors[cur_node] == 2:
            return False
        # cycle found
        if colors[cur_node] == 1:
            return True
        colors[cur_node] = 1

        for i in graph[cur_node]:
            cycle_found = self.hasCycle(i, colors, graph, top_sort)
            if cycle_found:
                return True
        # color nodes black as we backtrack
        colors[cur_node] = 2
        top_sort.append(cur_node)
        return False