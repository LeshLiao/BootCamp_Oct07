# function

'''
Please declare a function to calculate rectangle area

function name: rectangle_area
2 parameter: width, height

call the function rectangle_area(3,5)
if area greater than 10,
    print "big rectangle area = 15"

if area less than 10 or equal 10,
    print "normal rectangle area = 6"

ex:  rectangle_area(2,3)
normal rectangle area = 6

'''

def rectangle_area(width,height):
    area = width * height
    if area > 10:
        result = "big rectangle area = " + str(area)
        return result
    else:
        result = "normal rectangle area = " + str(area)
        return result

print(rectangle_area(2,3))