from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Using a prerequisite_map to map each course to it's prerequisites:
        prerequisite_map = defaultdict(list)
        for course, prereq in prerequisites:
            prerequisite_map[course].append(prereq)

        #Using DFS:
        #We use visited to keep track of the courses already visited (because this is a graph):
        visited = set()
        def dfs(course):
            #If we are back at the same course we already visited, that means there's a loop and we need to return False, because there is no way to complete these courses:
            if course in visited:
                return False
            #If there aren't any prerequisites for the course, then it's complete-able:
            if prerequisite_map[course] == []:
                return True 
            
            #Marking the course as visited:
            visited.add(course)
            
            #Recursively going through each course's prereqs and checking it with the dfs:
            for prereq in prerequisite_map[course]:
                #If there is a loop and dfs returns false, then return false for the main function as well:
                if not dfs(prereq):
                    return False

            #After going through the course entirely, and returning True, you can remove the course from the visited, but also set it's prerequisites to [] so that you don't check again for it: 
            visited.remove(course)
            prerequisite_map[course] = []
            return True
        
        #Excuting the dfs method on each course, if the dfs returns false entirely, then you return false, and true otherwise
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True