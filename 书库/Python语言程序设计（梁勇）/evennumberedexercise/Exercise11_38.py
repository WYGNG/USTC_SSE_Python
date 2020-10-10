import turtle
from UsefulTurtleFunctions import drawLine

# Draw a polyline to connect all the points in the list
def drawPolyline(points):
    for i in range(len(points) - 1):
        drawLine(points[i], points[i + 1])

# Draw a polygon to connect all the points in the list and 
# close the polygon by connecting the first point with the last point
def drawPolygon(points):
    drawPolyline(points)
    drawLine(points[len(points) - 1], points[0]) # Close the polygon

# Fill a polygon by connecting all the points in the list 
def fillPolygon(points):
    turtle.begin_fill()
    drawPolygon(points)
    turtle.end_fill()
