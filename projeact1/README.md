# update
- ฟังก์ชั่นดึงข้อมูลไฟล์ '.csv' และเลือกข้อมูลน้ำฝนระบุภูมิภาค ตั้งแต่ พ.ศ. 2548 - 2558
- ฟังก์ชั่นกราฟปริมาณน้ำฝนเฉลี่ยต่อปีตั้งแต่ พ.ศ. 2524 - 2558
- ฟังก์ชั่นกราฟปริมาณน้ำฝนแบบแยกภูมิภาคเทียบกับค่าเฉลี่ยในปีนั้นๆตั้งแต่ พ.ศ. 2548 - 2558
- ฟังก์ชั่นกราฟปริมาณน้ำฝนแบบทุกภาคเทียบค่าเฉลี่ยนปีนั้นๆตั้งแต่ พ.ศ. 2548 - 2558

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
    """อ่านข้อมูลแล้วส่งข้อมูลเป็น list ของแต่ละภาค"""
    url = open(r'2548-2558.csv')
    reader = csv.reader(url)
    return [float(i[count]) for i in reader]
```

## ฟังก์ชั่นกราฟปริมาณน้ำฝนเฉลี่ยต่อปีตั้งแต่ พ.ศ. 2524 - 2558

```
def plot_all():
    """ดึงข้อมูลน้ำฝนและแสดงผลเป็นกราฟ"""
    url = open(r'2524-2558.csv')
    reader = csv.reader(url)
    x = list(range(2524, 2559))
    y = [int(i[1]) for i in reader]
    aver = np.average(y)
    result = [aver for _ in range(len(y))]
    plt.bar(x, y)
    plt.plot(x, result, 'r')
    plt.xticks(x, rotation=45)
    plt.text(2558, aver, u'ค่าเฉลี่ยทั้งหมด 1458', fontname='JasmineUPC', fontsize='20')
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
```

# OUTPUT
`plot_all()`
![alt text](https://www.img.in.th/images/246e52cdd5d0dfd6510de4d1fa3eaaef.png)

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
