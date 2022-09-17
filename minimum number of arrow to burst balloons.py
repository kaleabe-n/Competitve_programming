class Solution(object):
    def findMinArrowShots(self, points):
        points.sort()
        arrows = 1
        intersection = None
        i = 0
        while i < len(points):
            changed = False
            if i == 0:
                intersection = points[i]
            elif intersection == None:
                intersection = points[i]
                arrows+=1
            elif intervalsConcide(intersection,points[i]):
                intersection = intersectionc(intersection,points[i])
            else:
                intersection = None
                i-=1
            i+=1
        return arrows
        """
        :type points: List[List[int]]
        :rtype: int
        """

        
def intervalsConcide(interval1,interval2):
    if interval1[1]>=interval2[0] and interval2[1] >=interval1[0]:
        return True
    return False
def intersectionc(interval1,interval2):
    return [max(interval1[0],interval2[0]),min(interval1[1],interval2[1])]
