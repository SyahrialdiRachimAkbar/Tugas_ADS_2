import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Exam Scores
nilai_ujian = [23, 60, 79, 32, 57, 74, 52, 70, 82, 36, 80, 77, 81, 95, 41, 65, 92, 85, 55, 76, 52, 10, 64, 75, 78, 25, 80, 98, 81, 67, 41, 71, 83, 54, 64, 72, 88, 62, 74, 43, 60, 78, 89, 76, 84, 48, 84, 90, 15, 79, 34, 67, 17, 82, 69, 74, 63, 80, 85, 61]
varians = np.var(nilai_ujian)
print("Varians: ", varians)
std_dev = np.sqrt(varians)
print("Standar Deviasi: ", std_dev)
