# def area(points):
#   x1, y1, x2, y2, x3, y3 = points
#   return 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

# with open('ProjectEuler/102_input.txt') as f:
#   temp = f.read().split()
#   points = [list(map(int, i.split(','))) for i in temp]

# # count = 0
# # for point in points:
# #   x1, y1, x2, y2, x3, y3 = point
# #   areas = [[x1, y1, x2, y2, 0, 0], [x1, y1, 0, 0, x3, y3], [0, 0, x2, y2, x3, y3]]
# #   total_area = sum([area(i) for i in areas])
# #   if total_area == area([x1, y1, x2, y2, x3, y3]):
# #     count+=1
# # print(count)


list1 = [10, 20, [100, 200], [2000, 500]]
list1[2][1].append(40)
print(list1 )