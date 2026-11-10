class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {num: [] for num in range(numCourses)}
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        q = collections.deque()
        
        visited = set()
        loop = set()
        output = []
        def dfs(course):
            if course in loop:
                return False
            if course in visited:
                return True
            loop.add(course)
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False
            loop.remove(course)
            visited.add(course)
            output.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return output

                

        