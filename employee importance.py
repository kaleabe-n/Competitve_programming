"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        empMap = {}
        for emp in employees:
            empMap[emp.id] = emp
        return helper(empMap[id],empMap)
        
        
def helper(node,empMap):
    currImp = node.importance
    for sub in node.subordinates:
        currImp+=helper(empMap[sub],empMap)
    return currImp





# """
# # Definition for Employee.
# class Employee(object):
#     def __init__(self, id, importance, subordinates):
#     	#################
#         :type id: int
#         :type importance: int
#         :type subordinates: List[int]
#         #################
#         self.id = id
#         self.importance = importance
#         self.subordinates = subordinates
# """

# class Solution(object):
#     def getImportance(self, employees, id):
#         def find(id,empMap):
#             employee = empMap[id]
#             imp = employee.importance
#             for i in employee.subordinates:
#                 imp+=find(i,empMap)
#             return imp
#         empMap = {}
#         for employee in employees:
#             empMap[employee.id] = employee
#         return find(id,empMap)
        
#         """
#         :type employees: List[Employee]
#         :type id: int
#         :rtype: int
#         """
        
