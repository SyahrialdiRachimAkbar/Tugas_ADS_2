#Data
Data = (919, 1196, 785, 1126, 936, 918,
        1156, 920, 948, 1067, 1092, 1162,
        1170, 929, 950, 905, 972, 1035,
        1045, 855, 1195, 1195, 1340, 1122,
        938, 970, 1237, 956, 1102, 1157,
        978, 832, 1009, 1157, 1151, 1009,
        765, 958, 902, 1022, 1333, 811,
        1217, 1085, 896, 958, 1311, 1037,
        702, 923)
Data = sorted(Data)  #Mengurutkan data
Q1 = Data[len(Data)//4]
median = Data[len(Data)//2]
Q3 = Data[3*len(Data)//4]
min_value = min(Data)
max_value = max(Data)
print (Q1, median, Q3, min_value, max_value)