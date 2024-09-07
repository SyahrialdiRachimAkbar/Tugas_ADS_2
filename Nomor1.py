import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Nilai ujian
nilai_ujian = [23, 60, 79, 32, 57, 74, 52, 70, 82, 36, 80, 77, 81, 95, 41, 65, 92, 85, 55, 76, 52, 10, 64, 75, 78, 25, 80, 98, 81, 67, 41, 71, 83, 54, 64, 72, 88, 62, 74, 43, 60, 78, 89, 76, 84, 48, 84, 90, 15, 79, 34, 67, 17, 82, 69, 74, 63, 80, 85, 61]

# a). Membuat stem-and-leaf plot
stems = [1, 2, 3, 4, 5, 6, 7, 8, 9]
leaves = []
for nilai in nilai_ujian:
    stem = nilai // 10
    leaf = nilai % 10
    leaves.append([stem, leaf])

plt.figure(figsize=(10, 6))
plt.subplot(111)
for i, stem in enumerate(stems):
    x = [leaf for s, leaf in leaves if s == stem]
    if x:
        plt.plot([i] * len(x), x, 'bo' if max(x) > 1 else 'bo', markersize=10)
plt.xticks(stems)
plt.yticks([])
plt.xlabel('Stem')
plt.ylabel('Leaf')
plt.title('Stem-and-Leaf Plot of Examination Grades')
plt.show()

# b). Membuat histogram serta skewnessnya dan mengambil kesimpulannya
# Membuat histogram relative frequency
plt.hist(nilai_ujian, bins=10, weights=[1/len(nilai_ujian)]*len(nilai_ujian), ec='black')
plt.xlabel('Nilai Ujian')
plt.ylabel('Frekuensi Relative')
plt.title('Histogram Nilai Ujian')
plt.show()

# Membuat kurva estimasi
mean, std = np.mean(nilai_ujian), np.std(nilai_ujian)
x = np.linspace(mean - 3*std, mean + 3*std, 100)
y = np.exp(-((x-mean)**2)/(2*std**2)) / (std * np.sqrt(2*np.pi))
plt.plot(x, y)
plt.xlabel('Nilai Ujian')
plt.ylabel('Frekuensi')
plt.title('Kurva Estimasi Nilai Ujian')
plt.show()

# Membuat discuss skewness
skewness = np.mean([(x-mean)/std**3 for x in nilai_ujian])
print('Skewness:', skewness)
if skewness > 0:
    print('Distribusi nilai ujian cenderung skewed ke kanan.')
elif skewness < 0:
    print('Distribusi nilai ujian cenderung skewed ke kiri.')
else:
    print('Distribusi nilai ujian simetris.')

