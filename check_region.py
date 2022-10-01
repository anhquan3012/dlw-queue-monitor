def is_in_side(region,point):
    x0=point[0]
    y0=point[1]
    x1=region['x1']
    y1=region['y1']
    x2=region['x2']
    y2=region['y2']
    x3=region['x3']
    y3=region['y3']
    x4=region['x4']
    y4=region['y4']
    S1=abs((x1-x0)*(y2-y0)-(x2-x0)*(y1-y0))/2.0
    S2=abs((x2-x0)*(y3-y0)-(x3-x0)*(y2-y0))/2.0
    S3=abs((x3-x0)*(y4-y0)-(x4-x0)*(y3-y0))/2.0
    S4=abs((x4-x0)*(y1-y0)-(x1-x0)*(y4-y0))/2.0
    S5=abs((x1-x2)*(y3-y2)-(x3-x2)*(y1-y2))/2.0
    S6=abs((x1-x4)*(y3-y4)-(x3-x4)*(y1-y4))/2.0
    if(abs(S1+S2+S3+S4-S5-S6)<=1e-6):
        return True
    else:
        return False
    
def in_region(point, regions):
    for id_region, region in regions.items():
        if is_in_side(region, point):
            return id_region
    return 0

def count_in_regions(regions, points):
    count = {k: 0 for k, v in regions.items()}
    count[0] = 0
    for point in points:
        count[in_region(point, regions)] += 1
    del count[0]
    return count
