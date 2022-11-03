# LeetCode 973


import heapq
import math

class Solution:
    def kClosest(self, points, k: int):
        
        # output array
        output = []
        # min heap for distances
        minHeap = []
        # key=distance value=array of the points
        hashTable = {}
        
        # loop through points
        for x,y in points:
            # calculate dist
            dist = math.sqrt((0-x)**2+(0-y)**2)
            # add distance to heap
            heapq.heappush(minHeap,dist)
            # add point to corresponding distance in hashtable
            if dist in hashTable:
                hashTable[dist].append([x,y])
            else:
                hashTable[dist] = [[x,y]]
        
        # pop elements from heap k times and append to output
        for i in range(k):
            dist = heapq.heappop(minHeap)
            if len(hashTable[dist]) > 1:
                output.append(hashTable[dist].pop(0))
            else:
                output.append(hashTable[dist][0])
            
        return output

# Time Complexity: O(klogn)
# Space Complexity: O(n)
class Solution:
    def kClosest(self, points, k: int):

        # initialize arrays
        output = []
        minHeap = []
        
        # loop through points, populate heap with calculated distance and points
        for x,y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist,x,y])
            
        # heapify the array
        heapq.heapify(minHeap)
        
        # pop from heap k times and append to output
        for i in range(k):
            dist, x, y = heapq.heappop(minHeap)
            output.append([x,y])
            
        return output
            