from __future__ import annotations
from typing import List

import collections
import heapq

from collections import deque
from utils import timeout

@timeout(5)
def mazeQ1b(graph: List[List[int]], start: List[int], end: List[int], F: int) -> int:
  i=len(graph)
  j=len(graph[0])

  queue = deque()
  visited=[]
  visited.append((1,start[0],start[1]))
  queue.append((0,1,start[0],start[1]))
  
  if F >= i+j-3:                
      F= i+j-2 

  if start[0]==end[0] and start[1]==end[1]:
      return 0
  
  if graph[start[0]][start[1]] == 1 or graph[end[0]][end[1]] == 1:
      return -1
  #steps=0
  
  #nowpox=start[0]
  #nowpoy=start[1]
  
  #stepslist=[]
    

  while queue:  
    steps,laser,nowpox,nowpoy = queue.popleft()        
    #m = queue.pop(0) 
    if nowpox == end[0] and nowpoy == end[1]:
#        print(steps)
        return steps+1 

    for a in range (2,F+1):
        for dx,dy in [(0,-1),(-1,0),(0,1),(1,0),(0,-a),(-a,0),(0,a),(a,0)]:
                if 0 <= (nowpox+dx) < i and 0 <= (nowpoy+dy) < j: 
                    if  (dx,dy)!= (0,-1) and (dx,dy)!=(-1,0) and (dx,dy)!=(0,1) and (dx,dy)!=(1,0):
                        if laser==1:   
                            if graph[(nowpox+dx)][(nowpoy+dy)]==0:                              
                                if (laser,nowpox+dx,nowpoy+dy) not in visited:
                                    if nowpox+dx == end[0] and nowpoy+dy == end[1]:
#                                        print(steps)
                                        return steps+1                                     
                                    visited.append((laser-1,nowpox+dx,nowpoy+dy))
                                    queue.append((steps+1,laser-1,nowpox+dx,nowpoy+dy))                      
#                                    print("F",nowpox+dx,nowpoy+dy,laser)
#                                    print("F",steps+1)
                                
                    elif graph[(nowpox+dx)][(nowpoy+dy)]==0:
                        if (laser,nowpox+dx,nowpoy+dy) not in visited:
                            if nowpox+dx == end[0] and nowpoy+dy == end[1]:
#                                print(steps)
                                return steps+1 
                            visited.append((laser,nowpox+dx,nowpoy+dy))
                            queue.append((steps+1,laser,nowpox+dx,nowpoy+dy)) 
#                            print("N",nowpox+dx,nowpoy+dy,laser)
#                            print("N",steps+1)
    if F==1:
        for dx,dy in [(0,-1),(-1,0),(0,1),(1,0)]:
            if 0 <= (nowpox+dx) < i and 0 <= (nowpoy+dy) < j:
                if graph[(nowpox+dx)][(nowpoy+dy)]==0:
                    if (laser,nowpox+dx,nowpoy+dy) not in visited:
                        visited.append((laser,nowpox+dx,nowpoy+dy))
                        queue.append((steps+1,laser,nowpox+dx,nowpoy+dy))
                    if nowpox+dx == end[0] and nowpoy+dy == end[1]:
#                                            print(steps+1)
                                            return steps+1

  return -1
  
#mazeQ1b([[0,1,0,0,1,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,1,0,0,1,0]],[0,0],[5, 5],4)



