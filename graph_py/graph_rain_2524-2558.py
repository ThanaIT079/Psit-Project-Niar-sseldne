"""กราฟข้อมูลน้ำฝน 2524 - 2558"""
import csv
import matplotlib.pyplot as plt
import numpy as np

def main():
    """ดึงข้อมูลน้ำฝนและแสดงผลเป็นกราฟ"""
    url = open(r'2524-2558.csv')
    reader = csv.reader(url)
    x = np.arange(2524, 2559)
    y = [int(i[1]) for i in reader]
    result = np.average(y)
    plt.bar(x, y)
    plt.plot(x, [result]*len(x), 'r')
    plt.xticks(x, rotation=45)
    plt.text(2557, result+4, u'ค่าเฉลี่ยทั้งหมด 1458 มม.', fontname='JasmineUPC', fontsize='20')
    plt.title(u'กราฟรวมปริมาณน้ำฝนในประเทศไทยเฉลี่ยต่อปี ตั้งแต่ปี พ.ศ. 2524 - 2558', fontname='JasmineUPC', fontsize='20')
    plt.xlabel(u'ปี พ.ศ.', fontname='JasmineUPC', fontsize='20')
    plt.ylabel(u'ปริมาณน้ำฝน(มม.)', fontname='JasmineUPC', fontsize='20')
    plt.show()

main()
