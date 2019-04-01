def calc_average(t1, t2, t3):
    total = t1 + t2 + t3
    average = total / 3
    return average


"""Nearest Neighbor Results: """

# n = 16:
# Nearest Neighbor Length: 423.3125953608072
time_1 = 0.0005548000335693359
time_2 = 0.0004467964172363281
time_3 = 0.00040793418884277344
print("n = 16 average: " + str(calc_average(time_1, time_2, time_3)))

# n = 156:
# Nearest Neighbor Length: 2375.905358510601
time_1 = 0.02779364585876465
time_2 = 0.022719621658325195
time_3 = 0.0223391056060791
print("n = 156 average: " + str(calc_average(time_1, time_2, time_3)))

# n = 625:
# Nearest Neighbor Length: 4522.357584491416
time_1 = 0.25165605545043945
time_2 = 0.25391530990600586
time_3 = 0.2617478370666504
print("n = 625 average: " + str(calc_average(time_1, time_2, time_3)))

# n = 2500:
# Nearest Neighbor Length: 9010.57138101488
time_1 = 3.8879952430725098
time_2 = 3.8988823890686035
time_3 = 3.8244783878326416
print("n = 2500 average: " + str(calc_average(time_1, time_2, time_3)))


# n = 10000:
# Nearest Neighbor Length: 17519.50542739831
time_1 = 65.23735165596008
time_2 = 64.99074172973633
time_3 = 63.7195930480957
print("n = 10000 average: " + str(calc_average(time_1, time_2, time_3)))


""" Optimal Results: """

# n = 4:
# Optimal Length: 96.28174358013813
time_1 = 0.0007109642028808594
time_2 = 0.0006473064422607422
time_3 = 0.0007288455963134766
print("n = 4 average: " + str(calc_average(time_1, time_2, time_3)))

# n = 6:
# Optimal Length: 246.6868521339407
time_1 = 0.014451265335083008
time_2 = 0.010953664779663086
time_3 = 0.011434793472290039
print("n = 6 average: " + str(calc_average(time_1, time_2, time_3)))

# n = 8:
# Optimal Length: 342.49218688013406
time_1 = 0.5244197845458984
time_2 = 0.5345902442932129
time_3 = 0.5276191234588623
print("n = 8 average: " + str(calc_average(time_1, time_2, time_3)))

# n = 9:
# Optimal Length: 528.6114406542857
time_1 = 5.244612693786621
time_2 = 5.16737174987793
time_3 = 5.148786544799805
print("n = 9 average: " + str(calc_average(time_1, time_2, time_3)))

# n = 10:
# Optimal Length: 284.74453951592324
time_1 = 56.74240326881409
time_2 = 57.04271936416626
time_3 = 56.49725961685181
print("n = 10 average: " + str(calc_average(time_1, time_2, time_3)))

# n = 11:
# Optimal Length: 592.8659995060084
time_1 = 732.413516998291
time_2 = 731.5091228485107
time_3 = 737.9375629425049
print("n = 11 average: " + str(calc_average(time_1, time_2, time_3)))


"""
Results:

n = 16 average: 0.0004698435465494792
n = 156 average: 0.02428412437438965
n = 625 average: 0.25577306747436523
n = 2500 average: 3.8704520066579184
n = 10000 average: 64.64922881126404

n = 4 average: 0.0006957054138183594
n = 6 average: 0.012279907862345377
n = 8 average: 0.5288763840993246
n = 9 average: 5.186923662821452
n = 10 average: 56.76079408327738
n = 11 average: 733.9534009297689

"""


