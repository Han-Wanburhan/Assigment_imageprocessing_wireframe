# อ่านข้อมูลจากไฟล์และแปลงเป็นรูปแบบที่ง่ายต่อการจัดเรียง
data = []
with open('infer_yolov5x/exp/labels/1_jpg.rf.1e6c887f7488d385f4cd7860a5e12b2a.txt', 'r') as file:
    for line in file:
        class_id, x, y, w, h = map(float, line.split())
        data.append((class_id, x, y, w, h))

# เรียงข้อมูลตามตำแหน่ง x และ y
sorted_data = sorted(data, key=lambda x: (x[1], x[2]))

# พิมพ์ผลลัพธ์
for item in sorted_data:
    class_id, x, y, w, h = item
    print(f"{int(class_id)} {x} {y} {w} {h}")
