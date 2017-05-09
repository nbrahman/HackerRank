import sys
from datetime import date


def Solution(da,ma,ya,de,me,ye):
    e = date(ye,me,de)
    a = date(ya,ma,da)
    fine=0
    if a.day>e.day and a.month==e.month and a.year==e.year:
        fine=(a.day - e.day) * 15
    if a.month>e.month and a.year==e.year:
        fine=(a.month-e.month)*500
    if a.year>e.year:
        fine=10000
    return fine

d1,m1,y1 = input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]
print(Solution(d1,m1,y1,d2,m2,y2))