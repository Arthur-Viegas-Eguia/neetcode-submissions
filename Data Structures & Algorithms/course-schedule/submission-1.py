class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        courses = {i:[] for i in range(numCourses)}
        for courseNum, coursePrereq in prerequisites:
            courses[courseNum].append(coursePrereq)
        print(courses)
        def dfs(course):
            if course in visited:
                return False
            if courses[course] == []:
                return True
            visited.add(course)
            for req in courses[course]:
                if not dfs(req):
                    return False
            visited.remove(course)
            courses[course] = []
            return True
            
        for num in range(numCourses):
            if not dfs(num):
                return False
        return True
        