from math import ceil
def paint_calc(height, width, cover):
    num_of_cans_area = ceil((height * width) / cover)
    print(f"You'll need {num_of_cans_area} cans of paint")



test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)