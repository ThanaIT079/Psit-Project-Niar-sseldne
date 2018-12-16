"""วิเคาระห์ปริมาณน้ำฝน"""

import csv
import matplotlib.pyplot as plt
import numpy as np

def plot_all():
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

def plot_location(index, color, locate):
    """
    กราฟเส้นของแต่ละภาค
    0 ---> ภาคเหนือ
    1----> ภาคตะวันออกเฉียงเหนือ
    2----> ภาคกลาง
    3----> ภาคตะวันออก
    4----> ภาคใต้ฝั่งตะวันตก
    5----> ภาคใต้ฝั่งตะวันออก
    6----> ค่าเฉลี่ยของแต่ละปี
    """
    year = np.arange(2548, 2559)
    data_location10 = [location(i) for i in range(1, 8)]
    plt.bar(year, data_location10[index], width=.35, color=color)
    plt.bar(year+.35, data_location10[6], width=.35, color='gray')
    plt.title(locate, fontname='JasmineUPC', fontsize='20')
    plt.xlabel(u'ปี พ.ศ.', fontname='JasmineUPC', fontsize='20')
    plt.ylabel(u'ปริมาณน้ำฝน(ลบ.ม.)', fontname='JasmineUPC', fontsize='20')
    plt.xticks(year, rotation=45)
    plt.show()
    
 def plot_location_all():
    """กราฟเส้นของรวมทุกภาค"""
    year = np.arange(2548, 2559)
    color = ['c', 'green', 'magenta', 'coral', 'royalblue', 'lightskyblue', "gray"]
    region = ["northern", "northeastern", "central", "western", "southwestern", "southeastern", "average"]
    data_location10 = [location(i) for i in range(1, 8)]
    style = 0
    for i in range(0, 7):
        plt.bar(year+style, data_location10[i], width=0.1, color=color[i], label=region[i])
        style += 0.1
    plt.xticks(year, rotation=45)
    plt.legend()
    plt.title(u'กราฟรวมปริมาณน้ำฝนทุกภาคในประเทศไทย ตั้งแต่ปี พ.ศ. 2548 - 2558', fontname='JasmineUPC', fontsize='20')
    plt.xlabel(u'ปี พ.ศ.', fontname='JasmineUPC', fontsize='20')
    plt.ylabel(u'ปริมาณน้ำฝน(มม.)', fontname='JasmineUPC', fontsize='20')
    plt.show()

def location(count):
    """อ่านข้อมูลแล้วส่งข้อมูลเป็น list ของแต่ละภาค"""
    url = open(r'2548-2558.csv')
    reader = csv.reader(url)
    return [float(i[count]) for i in reader]

"""
ส่วนของกราฟข้อมูลปริมาณน้ำฝนรวมรายปี ตั้งแต่ พ.ศ. 2524 - 2558
ทั้งหมด 35 ปี ในฟังก์ชั่น plot_all()
"""
plot_all()

"""
ส่วนของกราฟของแต่ละภาคเทียบกับค่าเฉลี่ยในแต่ละปี ตั้งแต่ พ.ศ. 2548 - 2558
ทั้งหมด 11 ปี
"""
plot_location(0, 'c', u'ข้อมูลน้ำฝนของภาคเหนือตั้งแต่ปี 2548 - 2558')
plot_location(1, 'green', u'ข้อมูลน้ำฝนของภาคตะวันออกเฉียงเหนือตั้งแต่ปี 2548 - 2558')
plot_location(2, 'magenta', u'ข้อมูลน้ำฝนของภาคกลางตั้งแต่ปี 2548 - 2558')
plot_location(3, 'lawngreen', u'ข้อมูลน้ำฝนของภาคตะวันออกตั้งแต่ปี 2548 - 2558')
plot_location(4, 'royalblue', u'ข้อมูลน้ำฝนของภาคใต้ฝั่งตะวันตกตั้งแต่ปี 2548 - 2558')
plot_location(5, 'lightskyblue', u'ข้อมูลน้ำฝนของภาคใต้ฝั่งตะวันออกตั้งแต่ปี 2548 - 2558')

"""
ส่วนของกราฟทุกภาค ตั้งแต่ พ.ศ. 2548 - 2558
"""
plot_location_all()
