"""กราฟข้อมูลน้ำฝน 2524 - 2558"""
import csv
import matplotlib.pyplot as plt
def main():
    """ดึงข้อมูลน้ำฝนและแสดงผลเป็นกราฟ"""
    url = open(r'2524-2558.csv')
    reader = csv.reader(url)
    x = list(range(2524, 2559))
    y = [int(i[1]) for i in reader]
    aver = sum(y) / len(y)
    result = [aver for _ in range(len(y))]
    plt.bar(x, y)
    plt.plot(x, result, 'r')
    plt.xticks(x, rotation=45)
    plt.text(2558, aver, u'ค่าเฉลี่ยทั้งหมด 1458', fontname='JasmineUPC', fontsize='20')
    plt.show()

main()
