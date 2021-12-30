class Solution(object):
    def kClosest(self, points, k):
        distances={}
        other=[]
        for i in points:
            distance=i[0]*i[0]+i[1]*i[1]
            distance=sqrt(distance)
            distances[distance]=i
            other.append(distance)
        repeated = False
        for i in range(len(other)-1):
            if other[i]==other[i+1]:
                repeated =True
        if repeated:
            distances=[]
            for i in points:
                distance=i[0]*i[0]+i[1]*i[1]
                distance=sqrt(distance)
                distances.append(distance)
            i=0
            while(i<len(points)):
                j=i
                m=distances[i]
                index=i
                while j<len(points):
                    if distances[j]<m:
                        m=distances[j]
                        index=j
                    j+=1
                points.insert(i,points.pop(index))
                distances.insert(i,distances.pop(index))
                if i==k:
                    break
                i+=1
                arr=points
        else:
            s=sorted(distances)
            arr=[]
            counter=0
            for i in s:
                arr.append(distances[i])
                if counter==k-1:
                    break
                counter+=1
        
        return arr[:k]
            
        
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
