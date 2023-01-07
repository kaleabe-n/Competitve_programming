#with O(1) extra space and O(n) time

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        operations = [None] * len(boxes)
        ops = 0
        balls = 0

        #find the number of operations for the last box
        for i in range(len(boxes)):
            ops += balls
            if boxes[i] == "1":
                balls += 1

        #find the number of operations by moving to the back shifting the sum at each iterations 
        ballsR = 0
        opsR = 0
        for i in range(len(boxes)-1,-1,-1):
            operations[i] = ops + opsR
            if boxes[i] == "1":
                balls -= 1
                ballsR += 1
            ops -= balls
            opsR += ballsR

        return operations


#with O(1) space and (N2) time

# class Solution:
#     def minOperations(self, boxes: str) -> List[int]:
#         operations = [None] * len(boxes)
#         #for each index find the number of operations by iterating from start to the index and from the end to the index
#         for i in range(len(boxes)):
#             ops = 0
#             balls = 0
#             for j in range(0,i):
#                 if boxes[j] == "1":
#                     balls+=1
#                 ops += balls
#             operations[i] = ops

#             ops =  0
#             balls = 0
#             for j in range(len(boxes)-1, i, -1):
#                 if boxes[j] == "1":
#                     balls+=1
#                 ops += balls
#             operations[i] += ops

#         return operations
