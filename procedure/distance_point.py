import numpy as np

lst2 = [35, 16, 105, 83]
lst1 = [34, 16, 108, 83]

def getPoint(lst: list):
    point_left_1 = tuple(lst[:2])
    point_right_1 = tuple(lst[2:])
    return (point_left_1, point_right_1)

def distance(pointA, pointB):
    x = (pointA[0]-pointB[0])**2
    y = (pointA[1]-pointB[1])**2
    dist = np.sqrt(x + y)
    return dist


left_distance = (distance(getPoint(lst1)[0], getPoint(lst2)[0]))
right_distance = (distance(getPoint(lst1)[1], getPoint(lst2)[1]))

if (left_distance < 2 and right_distance < 2):
    print("Display frame that sidewalk encroachment")
else:
    print(f"{left_distance, right_distance}")

