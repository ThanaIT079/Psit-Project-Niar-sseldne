"""

"""
import csv
import matplotlib.pyplot as plt
import numpy as np

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
    plt.show()

def location(count):
    """อ่านข้อมูลแล้วส่งข้อมูลเป็น list ของแต่ละภาค"""
    url = open(r'2548-2558.csv')
    reader = csv.reader(url)
    return [float(i[count]) for i in reader]

plot_location_2558()
