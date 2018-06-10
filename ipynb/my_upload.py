import math
from queue import PriorityQueue


#I have implemented the idea of https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes

def shortest_path(graph, start, goal):
    
    oSet = PriorityQueue()
    oSet.put(start, 0)
    
    previous = {start: None}
    goalScore = {start: 0}

    while not oSet.empty():
        current = oSet.get()

        if current == goal:
            path_reconstructing(previous, start, goal)

        for neighbor in graph.roads[current]:
            tempGoalScore = goalScore[current] + hxMeasure(graph.intersections[current], graph.intersections[neighbor])
            
            if neighbor not in goalScore or tempGoalScore < goalScore[neighbor]:
                goalScore[neighbor] = tempGoalScore
                totalScore = tempGoalScore + hxMeasure(graph.intersections[current], graph.intersections[neighbor])
                oSet.put(neighbor, totalScore)
                previous[neighbor] = current

    return path_reconstructing(previous, start, goal)


#returning distance from start to goal
def hxMeasure(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))

def path_reconstructing(previous, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = previous[current]
        path.append(current)
    path.reverse()
    return path