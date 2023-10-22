import os
import bs4

# html = """
#     <html>
#       <head>
#       </head>
#       <body>
#       </body>
#     </html>
#     """
def delete_in_body():
    with open("output.html", "r") as f:
        html = f.read()
    # แปลง HTML เป็น BeautifulSoup object
    soup = bs4.BeautifulSoup(html, "html.parser")
    body_tag = soup.find('body')
    body_tag.clear()
    html = str(soup)

    # สร้างไฟล์ HTML
    with open("output.html", "w") as f:
        f.write(html)

    print(f"สร้างไฟล์ HTML สำเร็จที่ {os.path.join(os.getcwd(), 'output.html')}")



def create_html_file(x):
    print("generate", x)
    # สร้างแหล่งข้อมูล HTML
    with open("output.html", "r") as f:
        html = f.read()

    # แปลง HTML เป็น BeautifulSoup object
    soup = bs4.BeautifulSoup(html, "html.parser")


    if x =="1":
        x = "input"
        add = soup.new_tag("input")
        add['type'] = 'checkbox'
        soup.body.append(add)
    
    elif x == '0':
        add = soup.new_tag('button')
        add.string = "Button"
        soup.body.append(add)

    elif x == "3":
        add = soup.new_tag('footer')
        add.string = "footer"
        soup.body.append(add)

    elif x == "5":
        x = "h1"
        add = soup.new_tag("h1")
        add.string = "heading"
        soup.body.append(add)

    elif x == "6":
        x = "input"
        add = soup.new_tag("input")
        add["type"]="text"
        soup.body.append(add)

    elif x == "7":
        x = 'nav'
        add = soup.new_tag('nav')
        add.string = "nav"
        soup.body.append(add)
    
    elif x == "2":
        add = soup.new_tag('div')
        add.string = "div"
        soup.body.append(add)
    
    elif x == "4":
        add = soup.new_tag('img')
        add['src'] = "https://www.the-sun.com/wp-content/uploads/sites/6/2023/10/www-instagram-com-monkeycatluna-hl-851711797.jpg"  
        add['width'] = '200'  # กำหนดความกว้าง
        add['height'] = '200'  # กำหนดความสูง
        soup.body.append(add)
    
    elif x == "8":
        add = soup.new_tag('p')
        add.string = "text"
        soup.body.append(add)

    soup = soup.prettify()




    html = str(soup)

    # สร้างไฟล์ HTML
    with open("output.html", "w") as f:
        f.write(html)

    print(f"สร้างไฟล์ HTML สำเร็จที่ {os.path.join(os.getcwd(), 'output.html')}")



# def create_sh_html_file():
#     # สร้างแหล่งข้อมูล HTML
#     with open("output.html", "r") as f:
#         html = f.read()

#     # แปลง HTML เป็น BeautifulSoup object
#     soup = bs4.BeautifulSoup(html, "html.parser")





#     html = str(soup)

#     # สร้างไฟล์ HTML
#     with open("shoutput.html", "w") as f:
#         f.write(html)

#     print(f"สร้างไฟล์ HTML สำเร็จที่ {os.path.join(os.getcwd(), 'output.html')}")


# def create_sh_html_file():
#     # สร้างแหล่งข้อมูล HTML
#     with open("output.html", "r") as f:
#         html = f.read()

#     # แปลง HTML เป็น BeautifulSoup object
#     soup = bs4.BeautifulSoup(html, "html.parser")

#     # สร้าง Tag <pre> และใส่ข้อมูล HTML ลงในนั้น
#     pre_tag = soup.new_tag("pre")
    
#     pre_tag.string = str(soup)

#     # สร้างไฟล์ HTML
#     with open("shoutput.html", "w") as f:
#         f.write(str(pre_tag))

#     print(f"สร้างไฟล์ HTML สำเร็จที่ {os.path.join(os.getcwd(), 'shoutput.html')}")

# # เรียกใช้ฟังก์ชัน
# create_sh_html_file()

def create_sh_html_file():
    # สร้างแหล่งข้อมูล HTML
    with open("output.html", "r") as f:
        html = f.read()

    # แปลง HTML เป็น BeautifulSoup object
    soup = bs4.BeautifulSoup(html, "html.parser")

    # สร้าง Tag <pre> และใส่ข้อมูล HTML ลงในนั้น
    pre_tag = soup.new_tag("pre")

    # แปลง HTML เป็น HTML entities
    pre_tag.string = bs4.NavigableString(str(soup).replace('<', '&lt;').replace('>', '&gt;'))
    
    pre_tag.string = bs4.NavigableString(str(soup).replace('amp;', '').replace('amp;', ''))
    # สร้างไฟล์ HTML
    with open("shoutput.html", "w") as f:
        f.write(str(pre_tag))

    print(f"สร้างไฟล์ HTML สำเร็จที่ {os.path.join(os.getcwd(), 'shoutput.html')}")

# create_sh_html_file()
