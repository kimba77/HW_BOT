# class_points = [2, 3, 100, 70, 40]
# your_points = 74
#
# a = sum(class_points) // len(class_points)
#
#
# def better_than_avarage(class_points, your_points):
#     if (sum(class_points) // len(class_points)) < your_points:
#         return True
#     else:
#         return False
#
# print(a)





def konvert_dollars_to_uans(d):
    return "{:,.3f}".format(d * 6.75)


print(konvert_dollars_to_uans(23))