class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order =[]
        que = deque()

        graph = [ [] for _ in range(numCourses)]

        incoming = [ 0 for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)
            # count the pre req each course has
            incoming[course] +=1
        
        for course in range(numCourses):
            if incoming[course] == 0:
                que.append(course)
        while que:
            course = que.popleft()
            order.append(course)

            for neighbour in graph[course]:
                # reliefe the courses from their prerequsit count
                # because this one is bieng removed
                incoming[neighbour] -=1

                if incoming[neighbour] ==0:
                    que.append(neighbour)
                
        if len(order) != numCourses:
            return []
        return order



