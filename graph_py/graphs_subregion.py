"""
value of location
0 ---> ภาคเหนือ
1----> ภาคตะวันออกเฉียงเหนือ
2----> ภาคกลาง
3----> ภาคตะวันออก
4----> ภาคใต้ฝั่งตะวันตก
5----> ภาคใต้ฝั่งตะวันตก
6----> ค่าเฉลี่ยของแต่ละปี

"""
import csv
import matplotlib.pyplot as plt
import numpy as np
def plot_location(index, color, locate):
    """กราฟเส้นของแต่ละภาค"""
    year = np.arange(2548, 2559)
    data_location10 = [location(i) for i in range(1, 8)]
    plt.bar(year, data_location10[index], width=.35, color=color, label='region')
    plt.bar(year+.35, data_location10[6], width=.35, color='gray', label='total average')
    plt.title(locate, fontname='JasmineUPC', fontsize='20')
    plt.xlabel(u'ปี พ.ศ.', fontname='JasmineUPC', fontsize='20')
    plt.ylabel(u'ปริมาณน้ำฝน(มม.)', fontname='JasmineUPC', fontsize='20')
    plt.xticks(year, rotation=45)
    average_plot = np.average(data_location10[index])
    plt.plot(np.arange(2548, 2560), [average_plot-10]*12, 'r--', label='average region')
    plt.text(2558, average_plot, u'average region is = %.2f mm' %average_plot, color='r')
    plt.grid(axis='y', alpha=0.75)
    plt.legend()
    plt.show()

def location(count):
    """อ่านข้อมูลแล้วส่งข้อมูลเป็น list ของแต่ละภาค"""
    url = open(r'2548-2558.csv')
    reader = csv.reader(url)
    return [float(i[count]) for i in reader]

plot_location(0, 'c', u'ข้อมูลน้ำฝนของภาคเหนือตั้งแต่ปี 2548 - 2558')
plot_location(1, 'green', u'ข้อมูลน้ำฝนของภาคตะวันออกเฉียงเหนือตั้งแต่ปี 2548 - 2558')
plot_location(2, 'magenta', u'ข้อมูลน้ำฝนของภาคกลางตั้งแต่ปี 2548 - 2558')
plot_location(3, 'coral', u'ข้อมูลน้ำฝนของภาคตะวันตกตั้งแต่ปี 2548 - 2558')
plot_location(4, 'royalblue', u'ข้อมูลน้ำฝนของภาคใต้ฝั่งตะวันตกตั้งแต่ปี 2548 - 2558')
plot_location(5, 'lightskyblue', u'ข้อมูลน้ำฝนของภาคใต้ฝั่งตะวันออกตั้งแต่ปี 2548 - 2558')
