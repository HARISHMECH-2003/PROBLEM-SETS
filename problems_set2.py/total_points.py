def total_points(matches):
    total_points=0
    for result in matches:
        x,y=result
        if x>y:
            total_points+=3
        elif x==y:
            total_points+=1
    
    return total_points

matches=[[2,1],[3,0],[0,1],[3,1],[1,1]]
points=total_points(matches)
print(points)    