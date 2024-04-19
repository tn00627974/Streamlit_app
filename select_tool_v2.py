import json
import toml
import mysql.connector

# Reading data
toml_data = toml.load(".streamlit/secrets.toml")
# saving each credential into a variable

# 將 toml_data 中的屬性取出
host = toml_data["mysql"]["host"]
port = toml_data["mysql"]["port"]
user = toml_data["mysql"]["username"]
passwd = toml_data["mysql"]["password"]
db = toml_data["mysql"]["database"]
charset = "utf8"  # 或其他適當的字符集


def select_1(product_id):
    conn = mysql.connector.connect(
        host=host, port=port, user=user, passwd=passwd, db=db, charset=charset
    )
    print("Successfully connected!")
    cursor = conn.cursor()

    sql = f"""
    select ID, 簡稱, 平均分數, 效果, 優點, 缺點, 推薦1, 推薦2, 推薦3 from items_table
    where ID = {product_id};
    """
    cursor.execute(sql)
    data = cursor.fetchone()

    cursor.close()
    conn.close()

    return data


def select_2(product_id, age_type):
    conn = conn = mysql.connector.connect(
        host=host, port=port, user=user, passwd=passwd, db=db, charset=charset
    )
    print("Successfully connected!")
    cursor = conn.cursor()

    sql = f"""
    select {age_type}分數, {age_type}效果 from items_table
    where ID = {product_id};
    """
    cursor.execute(sql)
    data = cursor.fetchone()

    cursor.close()
    conn.close()

    return data


def stars_1(js, math):
    star = {"type": "icon", "size": "lg", "url": "https://imgur.com/ZCwfMp0.png"}

    starhelf = {"type": "icon", "size": "lg", "url": "https://imgur.com/eIiB8Qn.png"}

    starlast = {
        "type": "text",
        "text": f"{math}",
        "size": "sm",
        "margin": "md",
        "color": "#111111",
        "offsetTop": "none",
        "offsetBottom": "none",
        "offsetStart": "none",
        "offsetEnd": "none",
    }

    for i in range(int(math)):
        js["body"]["contents"][2]["contents"].append(star)

    num = int(math * 10 % 10)
    if num >= 7 and num <= 9:
        js["body"]["contents"][2]["contents"].append(star)
        js["body"]["contents"][2]["contents"].append(starlast)
    elif num >= 4 and num <= 6:
        js["body"]["contents"][2]["contents"].append(starhelf)
        js["body"]["contents"][2]["contents"].append(starlast)
    else:
        js["body"]["contents"][2]["contents"].append(starlast)

    return js


def stars_2(js, math, info_number):
    star = {"type": "icon", "size": "lg", "url": "https://imgur.com/ZCwfMp0.png"}

    starhelf = {"type": "icon", "size": "lg", "url": "https://imgur.com/eIiB8Qn.png"}

    starlast = {
        "type": "text",
        "text": f"{math}",
        "size": "sm",
        "margin": "md",
        "color": "#111111",
        "offsetTop": "none",
        "offsetBottom": "none",
        "offsetStart": "none",
        "offsetEnd": "none",
    }

    for i in range(int(math)):
        js["contents"][info_number]["body"]["contents"][2]["contents"].append(star)

    num = int(math * 10 % 10)
    if num >= 7 and num <= 9:
        js["contents"][info_number]["body"]["contents"][2]["contents"].append(star)
        js["contents"][info_number]["body"]["contents"][2]["contents"].append(starlast)
    elif num >= 4 and num <= 6:
        js["contents"][info_number]["body"]["contents"][2]["contents"].append(starhelf)
        js["contents"][info_number]["body"]["contents"][2]["contents"].append(starlast)
    else:
        js["contents"][info_number]["body"]["contents"][2]["contents"].append(starlast)

    return js


def load_js1(data):
    with open("v1.json", mode="r", encoding="utf-8") as fi:
        js = json.load(fi)

    math = data[2]
    js = stars_1(js, math)
    # 修改 "hero" 中的 "url"
    js["hero"]["url"] = image_dict[data[0]]  # 抓
    js["body"]["contents"][0]["text"] = mark[data[0]]  # 品牌
    js["body"]["contents"][1]["text"] = data[1]  # 商品名稱
    js["body"]["contents"][3]["contents"][0]["contents"][1]["text"] = data[3]  # 效果
    js["body"]["contents"][3]["contents"][1]["contents"][1]["text"] = data[4]  # 優點
    js["body"]["contents"][3]["contents"][1]["contents"][2]["contents"][1]["text"] = (
        data[5]
    )  # 缺點
    js["footer"]["contents"][1]["action"]["text"] = f"推薦:{data[1]}"  # 推薦商品
    # js["contents"]["footer"]["contents"][0]["action"]["uri"] = product_url_dict[data[0]]
    js["footer"]["contents"][0]["action"]["uri"] = product_url_dict[
        data[0]
    ]  # 推薦商品三種 url

    return js


def load_js2(data):
    with open("v2.json", mode="r", encoding="utf-8") as fi:
        js = json.load(fi)

    for info_number in range(3):
        math = data[info_number][2]
        js = stars_2(js, math, info_number)

        js["contents"][info_number]["hero"]["url"] = image_dict[data[info_number][0]]

        js["contents"][info_number]["body"]["contents"][0]["text"] = mark[
            data[info_number][0]
        ]  # 品牌
        js["contents"][info_number]["body"]["contents"][1]["text"] = data[info_number][
            1
        ]  # 商品名稱
        js["contents"][info_number]["body"]["contents"][3]["contents"][0]["contents"][
            1
        ]["text"] = data[info_number][
            3
        ]  # 效果
        js["contents"][info_number]["body"]["contents"][3]["contents"][1]["contents"][
            1
        ]["text"] = data[info_number][
            4
        ]  # 優點
        js["contents"][info_number]["body"]["contents"][3]["contents"][1]["contents"][
            2
        ]["contents"][1]["text"] = data[info_number][
            5
        ]  # 缺點
        js["contents"][info_number]["footer"]["contents"][1]["action"][
            "text"
        ] = f"推薦:{data[info_number][1]}"  # 推薦商品
        js["contents"][info_number]["footer"]["contents"][0]["action"]["uri"] = (
            product_url_dict[data[info_number][0]]
        )

    return js


# 載入本機圖片路徑/face_rank


def push_db(id_tp):
    conn = conn = mysql.connector.connect(
        host=host, port=port, user=user, passwd=passwd, db=db, charset=charset
    )
    print("Successfully connected!")
    cursor = conn.cursor()

    sql = f"""
    select ID, 簡稱, 平均分數, 效果, 優點, 缺點, 推薦1, 推薦2, 推薦3 from items_table
    where ID = {id_tp[0]} or ID = {id_tp[1]} or ID = {id_tp[2]};
    """
    cursor.execute(sql)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data
