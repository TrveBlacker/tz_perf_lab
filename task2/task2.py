
# print("enter file 1 path")
circle_coord_file_name = input()
# print("enter file 2 path")
point_coord_file_name = input()

results = []

with open(circle_coord_file_name, "r") as circle_coord_file:
    circle_coord = circle_coord_file.read()
    circle_coord = circle_coord.splitlines()
    x_r, y_r = circle_coord[0].split()
    r = circle_coord[1]
    # print(circle_coord)

with open(point_coord_file_name, "r") as point_coord_file:
    point_coord = point_coord_file.read()
    point_coord = point_coord.splitlines()
    # print(point_coord)

def check_point_position(x_r, y_r, r, x_p, y_p):
    square_distance = (x_r - x_p)**2 + (y_r - y_p)**2 # Center to point distance squared

    if square_distance == r**2:
        return(0)
    elif square_distance < r**2:
        return(1)
    else:
        return(2)

for ind in range (len(point_coord)):
    x_p, y_p = point_coord[ind].split()
    result = check_point_position(float(x_r), float(y_r), float(r), float(x_p), float(y_p))
    print(result)

input()