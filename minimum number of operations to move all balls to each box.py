class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        operations = [None] * len(boxes)
        #for each index find the number of operations by iterating from start to the index and from the end to the index
        for i in range(len(boxes)):
            ops = 0
            balls = 0
            for j in range(0,i):
                if boxes[j] == "1":
                    balls+=1
                ops += balls
            operations[i] = ops

            ops =  0
            balls = 0
            for j in range(len(boxes)-1, i, -1):
                if boxes[j] == "1":
                    balls+=1
                ops += balls
            operations[i] += ops

        return operations
