from __future__ import annotations
from typing import List

import collections
import heapq

from collections import deque
from utils import timeout

@timeout(10)

def mazeQ1a(graph: List[List[int]], start: List[int], end: List[int]) -> int:
  i=len(graph)
  j=len(graph[0])

  queue = deque()
  visited=[]
  visited.append((start[0],start[1]))
  queue.append((0,start[0],start[1]))

  if start[0]==end[0] and start[1]==end[1]:
      return 0
  
  if graph[start[0]][start[1]] == 1 or graph[end[0]][end[1]] == 1:
      return -1
  #steps=0
  
  #nowpox=start[0]
  #nowpoy=start[1]
  
  #stepslist=[]
    

  while queue:  
    steps,nowpox,nowpoy = queue.popleft()        
    #m = queue.pop(0) 
    if nowpox == end[0] and nowpoy == end[1]:
      return steps
    for dx,dy in [(0,-1),(-1,0),(0,1),(1,0)]:
      if 0 <= (nowpox+dx) < i and 0 <= (nowpoy+dy) < j:
        if graph[(nowpox+dx)][(nowpoy+dy)]==0:
          if (nowpox+dx,nowpoy+dy) not in visited:
            visited.append((nowpox+dx,nowpoy+dy))
            queue.append((steps+1,nowpox+dx,nowpoy+dy))
     
  else:
    return -1


  
  
    