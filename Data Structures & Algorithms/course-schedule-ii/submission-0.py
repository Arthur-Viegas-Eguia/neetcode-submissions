class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseList = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            courseList[course].append(prereq)
        output = []
        visited, taken = set(), set()
        def dfs(course):
            if course in visited:
                return False
            if course in taken:
                return True
            visited.add(course)
            
            for pr in courseList[course]:
                if not dfs(pr):
                    return False
            if course not in taken:
                output.append(course)
            visited.remove(course)
            taken.add(course)
            return True
        for cours in range(numCourses):
            if not dfs(cours):
                return []
        return output
        