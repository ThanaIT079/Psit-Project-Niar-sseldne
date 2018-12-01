# update
- ดึงข้อมูลจากไฟล์ .csv
- เก็บข้อมูลลงใน list
- สร้างกราฟแท่งรูปแบบเริ่มต้น
- มีเส้นบอกค่าเฉลีี่ยทั้งหมด
- จัดรูปแบบการแสดงผลของเลขปีในแกน x แบบตัวเอียง

## กราฟข้อมูลปริมาณน้ำฝนตั้งแต่ปี พ.ศ. 2524 - 2558 แบบต่อปี

```
    import csv
    import matplotlib.pyplot as plt
```
- module csv ดึงข้อมูลน้ำฝนจากไฟล์ .csv
- module matplotlib.pyplot สร้างกราฟ

## ส่วนของการดึงข้อมูล และเก็บค่าข้อมูลเป็นประเภท list

```
    url = open(r'2524-2558.csv')
    reader = csv.reader(url)
    x = list(range(2524, 2559))
    y = [int(i[1]) for i in reader]
    aver = sum(y) / len(y)
    result = [aver for _ in range(len(y))]
```

## ส่วนของการสร้างกราฟและแสดงผลในรูปแบบกราฟแท่ง

```
    plt.bar(x, y)
    plt.plot(x, result, 'r')
    plt.xticks(x, rotation=45)
    plt.text(2558, aver, u'ค่าเฉลี่ยทั้งหมด 1458', fontname='JasmineUPC', fontsize='20')
    plt.show()
```

# OUTPUT
![alt text](https://www.img.in.th/images/246e52cdd5d0dfd6510de4d1fa3eaaef.png)
