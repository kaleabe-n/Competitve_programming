from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        freq = defaultdict(lambda:0)
        for i in nums:
            freq[i]+=1
        elements = list(freq.keys())
        heap = [None]
        for i in range(k):
            heap.append(elements[i])
            heapUp(heap,i+1,freq)
        for i in range(k,len(elements)):
            if freq[heap[1]]<freq[elements[i]]:
                heap[1] = elements[i]
                heapDown(heap,1,freq)
        # print([freq[x] for x in elements])
        # print(elements)
        # print([freq[x] for x in heap[1:]])
        return heap[1:]

def heapDown(heap,index,di):
    if index*2<len(heap) and di[heap[index*2]]<di[heap[index]]:
        heap[index],heap[index*2] = heap[index*2],heap[index]
        heapDown(heap,index*2,di)
        if index*2+1<len(heap) and di[heap[index*2+1]]<di[heap[index]]:
            heap[index*2+1],heap[index] = heap[index],heap[index*2+1]
            heapDown(heap,index*2+1,di)
    elif index*2+1<len(heap) and di[heap[index*2+1]]<di[heap[index]]:
        heap[index*2+1],heap[index] = heap[index],heap[index*2+1]
        heapDown(heap,index*2+1,di)
        if index*2<len(heap) and di[heap[index*2]]<di[heap[index]]:
            heap[index],heap[index*2] = heap[index*2],heap[index]
            heapDown(heap,index*2,di)
    else:
        return
def heapUp(heap,index,di):
    if index>1 and di[heap[index]]<di[heap[index//2]]: 
        heap[index],heap[index//2] = heap[index//2],heap[index]
        heapUp(heap,index//2,di)
    else:
        return
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
