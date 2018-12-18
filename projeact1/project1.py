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

def add_text(var_x, var_y, count1, count2):
    """เพิ่มตัวเลข"""
    for i in range(len(var_x)):
        rain = '%.2f' %var_y[i]
        rain = rain.rstrip("0")
        if i != 1:
            plt.text(var_x[i], var_y[i]+count1, u'%s' %rain, fontsize=24, style='oblique', ha='center', fontname='EucrosiaUPC')
        else:
            plt.text(var_x[i], var_y[i]+count2, u'%s' %rain, fontsize=24, style='oblique', ha='center', fontname='EucrosiaUPC')

def plot_location_2558():
    """กราฟเส้นของแต่ละภาค"""
    url = open(r'2548-2558.csv')
    reader = list(csv.reader(url))
    data_year = [float(i) for i in reader[-1][1:]]
    color = ['c', 'green', 'magenta', 'coral', 'royalblue', 'lightskyblue']
    region = ["northern", "northeastern", "central", "western", "southwestern", "southeastern"]
    plt.bar(region, data_year[:-1], color=color, width=0.5)
    plt.plot(region, [data_year[-1]]*6, 'r--')
    plt.title(u'กราฟข้อมูลปริมาณน้ำฝนในปี พ.ศ. 2558', fontname='JasmineUPC', fontsize='20')
    plt.xlabel(u'ภูมิภาค', fontname='JasmineUPC', fontsize='20')
    plt.ylabel(u'ปริมาณน้ำฝน(มม.)', fontname='JasmineUPC', fontsize='20')
    plt.text(region[0], data_year[-1]+15, u'average is = %.2f mm' %data_year[-1])
    plt.grid(axis='y', alpha=0.75)
    add_text(region, data_year[:-1], 40, 160)
    plt.show()
    
def plot_region_rank():
    """กราฟเส้นของแต่ละภาค"""
    region = ["northern", "northeastern", "central", "western", "southwestern", "southeastern"]
    dct_average, dct_color = {}, {}
    color = ['c', 'green', 'magenta', 'coral', 'royalblue', 'lightskyblue']
    for i in range(1, 7):
        result = np.average(location(i))
        dct_average[region[i-1]] = result
        dct_color[color[i-1]] = result
    region.sort(key=lambda x: dct_average[x])
    color.sort(key=lambda x: dct_color[x])
    rain = [dct_average[i] for i in region]
    plt.bar(region, rain, color=color, width=0.5)
    plt.title(u'กราฟเรียงลำดับภูมิภาคจากระดับน้ำฝนเฉลี่ยทั้งหมดจากน้อยไปมาก', fontname='JasmineUPC', fontsize='20')
    plt.xlabel(u'ภูมิภาค', fontname='JasmineUPC', fontsize='20')
    plt.ylabel(u'ปริมาณน้ำฝน(มม.)', fontname='JasmineUPC', fontsize='20')
    add_text(region, rain, 40, 40)
    plt.show()

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

"""
ส่วนของกราฟทุกภาคในปี พ.ศ. 2558
"""
plot_location_2558()

"""
ส่วนของกราฟทุกภาคเรียงจากน้อยไปมาก
"""
plot_region_rank()
