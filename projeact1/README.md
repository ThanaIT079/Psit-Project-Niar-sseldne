# update
- ฟังก์ชั่นดึงข้อมูลไฟล์ '.csv' และเลือกข้อมูลน้ำฝนระบุภูมิภาค ตั้งแต่ พ.ศ. 2548 - 2558
- ฟังก์ชั่นระบุตัวเลขค่าปริมาณน้ำฝน
- ฟังก์ชั่นกราฟปริมาณน้ำฝนเฉลี่ยต่อปีตั้งแต่ พ.ศ. 2524 - 2558
- ฟังก์ชั่นกราฟปริมาณน้ำฝนแบบแยกภูมิภาคเทียบกับค่าเฉลี่ยในปีนั้นๆตั้งแต่ พ.ศ. 2548 - 2558
- ฟังก์ชั่นกราฟปริมาณน้ำฝนแบบทุกภาคเทียบค่าเฉลี่ยนปีนั้นๆตั้งแต่ พ.ศ. 2548 - 2558
- ฟังก์ชั่นกราฟปริมาณน้ำฝนภูมิภาคปี พ.ศ. 2558
- ฟังก์ชั่นกราฟเรียงปริมาณน้ำฝนภูมิภาคจากน้อยไปมาก พ.ศ. 2524 - 2558

```
    import csv
    import matplotlib.pyplot as plt
    import numpy as np
```
- module csv ดึงข้อมูลน้ำฝนจากไฟล์ .csv
- module matplotlib.pyplot สร้างกราฟ
- module numpy คำนวนค่าเฉลี่ย บวกเลขหลายๆจำนวนแบบรวดเร็ว

## ฟังก์ชั่นดึงข้อมูลไฟล์และเลือกข้อมูลน้ำฝนระบุภูมิภาคตั้งแต่ พ.ศ. 2548 - 2558

```
def location(count):
    url = open(r'2548-2558.csv')
    reader = csv.reader(url)
    return [float(i[count]) for i in reader]
```

## ฟังก์ชั่นระบุตัวเลขปริมาณน้ำฝน

```
def add_text(var_x, var_y, count1, count2):
    """เพิ่มตัวเลข"""
    for i in range(len(var_x)):
        rain = '%.2f' %var_y[i]
        rain = rain.rstrip("0")
        if i != 1:
            plt.text(var_x[i], var_y[i]+count1, u'%s' %rain, fontsize=24, style='oblique', ha='center', fontname='EucrosiaUPC')
        else:
            plt.text(var_x[i], var_y[i]+count2, u'%s' %rain, fontsize=24, style='oblique', ha='center', fontname='EucrosiaUPC')
```

## ฟังก์ชั่นกราฟปริมาณน้ำฝนเฉลี่ยต่อปีตั้งแต่ พ.ศ. 2524 - 2558

```
def plot_all():
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
    color = list(map(lambda x: '#1f77b4' if x >= result else 'r', y))
    plt.bar(x, y, color=color)
    plt.plot(x, [result]*len(x), 'r')
    plt.xticks(x, rotation=45)
    plt.text(2557, result+4, u'ค่าเฉลี่ยทั้งหมด 1458 มม.', fontname='JasmineUPC', fontsize='20')
    plt.show()
```

## ฟังก์ชั่นกราฟปริมาณน้ำฝนเฉลี่ยต่อปีตั้งแต่ พ.ศ. 2524 - 2558

```
def plot_location(index, color, locate):
    year = np.arange(2548, 2559)
    data_location10 = [location(i) for i in range(1, 8)]
    plt.bar(year, data_location10[index], width=.35, color=color)
    plt.bar(year+.35, data_location10[6], width=.35, color='gray')
    plt.title(locate, fontname='JasmineUPC', fontsize='20')
    plt.xlabel(u'ปี พ.ศ.', fontname='JasmineUPC', fontsize='20')
    plt.ylabel(u'ปริมาณน้ำฝน(ลบ.ม.)', fontname='JasmineUPC', fontsize='20')
    plt.xticks(year, rotation=45)
    plt.show()
```

## ฟังก์ชั่นกราฟปริมาณน้ำฝนแบบทุกภาคเทียบค่าเฉลี่ยปีนั้นๆตั้งแต่ พ.ศ. 2548 - 2558

```
def plot_location_all():
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
```
## ฟังก์ชั่นกราฟปริมาณน้ำฝนภูมิภาคปี พ.ศ. 2558

```
def plot_location_2558():
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
```

## ฟังก์ชั่นกราฟเรียงปริมาณน้ำฝนภูมิภาคจากน้อยไปมาก พ.ศ. 2524 - 2558

```
def plot_region_rank():
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
```

# OUTPUT
`plot_all()`
![f41e701ea08fd752e0e5d090323073f8.png](https://www.img.in.th/images/f41e701ea08fd752e0e5d090323073f8.png)

![4ef409899ae0a57dad30291d1eee5be5.png](https://www.img.in.th/images/4ef409899ae0a57dad30291d1eee5be5.png)

`plot_location(0, 'c', u'ข้อมูลน้ำฝนของภาคเหนือตั้งแต่ปี 2548 - 2558')`
![24f761eb4131573afede6bc40fb08078.png](https://www.img.in.th/images/24f761eb4131573afede6bc40fb08078.png)

`plot_location(1, 'green', u'ข้อมูลน้ำฝนของภาคตะวันออกเฉียงเหนือตั้งแต่ปี 2548 - 2558')`
![609f1789a2e75dbbf2a6836977abd1b4.png](https://www.img.in.th/images/609f1789a2e75dbbf2a6836977abd1b4.png)

`plot_location(2, 'magenta', u'ข้อมูลน้ำฝนของภาคกลางตั้งแต่ปี 2548 - 2558')`
![be4ab453e346894a7f65031d7b6abd39.png](https://www.img.in.th/images/be4ab453e346894a7f65031d7b6abd39.png)

`plot_location(3, 'coral', u'ข้อมูลน้ำฝนของภาคตะวันตกตั้งแต่ปี 2548 - 2558')`
![ef094f91e25f678d0de1383bbb58da66.png](https://www.img.in.th/images/ef094f91e25f678d0de1383bbb58da66.png)

`plot_location(4, 'royalblue', u'ข้อมูลน้ำฝนของภาคใต้ฝั่งตะวันตกตั้งแต่ปี 2548 - 2558')`
![6f31c61e9dce2a3257929cd8329dcc15.png](https://www.img.in.th/images/6f31c61e9dce2a3257929cd8329dcc15.png)

`plot_location(5, 'lightskyblue', u'ข้อมูลน้ำฝนของภาคใต้ฝั่งตะวันออกตั้งแต่ปี 2548 - 2558')`
![4f9454c77ab339c8d448a59dc2a696b3.png](https://www.img.in.th/images/4f9454c77ab339c8d448a59dc2a696b3.png)

`plot_location_all()`
![978fcbf17811ed57b819e2a11dc454cb.png](https://www.img.in.th/images/978fcbf17811ed57b819e2a11dc454cb.png)

`plot_location_2558()`
![f71bcba6cc958cde02b78cfe7b5e5f58.png](https://www.img.in.th/images/f71bcba6cc958cde02b78cfe7b5e5f58.png)

`plot_region_rank()`
![f2bfaebbcd7372ebbf235cc2e17f4728.jpg](https://www.img.in.th/images/f2bfaebbcd7372ebbf235cc2e17f4728.jpg)
