import json
import toml
import mysql.connector

# import configparser
# config = configparser.ConfigParser()
# config.read('config.ini')

# Reading data
toml_data = toml.load(".streamlit/secrets.toml")
# saving each credential into a variable

# # 將 toml_data 中的屬性取出
# host = toml_data["mysql"]["host"]
# port = toml_data["mysql"]["port"]
# user = toml_data["mysql"]["username"]
# passwd = toml_data["mysql"]["password"]
# db = toml_data["mysql"]["database"]
# charset = "utf8"  # 或其他適當的字符集

mark = {
    0: "FOAM",
    1: "上山採藥",
    2: "卵肌",
    3: "極潤",
    4: "極潤",
    5: "豆乳",
    6: "草本",
    7: "Simple",
    8: "Perfect Whip",
    9: "雪肌粹",
    10: "Biore",
    11: "Biore",
    12: "Bifesta",
    13: "Biore",
    14: "草本",
    15: "Bifesta",
    16: "Bifesta",
    17: "Bifesta",
}


# image_dict = {
#     0: "https://imgur.com/ojqgngi.jpg",
#     1: "https://imgur.com/tlAiF6h.jpg",
#     2: "https://imgur.com/GMueS4b.jpg",
#     3: "https://imgur.com/N9Omj8j.jpg",
#     4: "https://imgur.com/jYEZal6.jpg",
#     5: "https://imgur.com/OmgeQOn.jpg",
#     6: "https://imgur.com/JLAYFzr.jpg",
#     7: "https://imgur.com/q3mgxPe.jpg",
#     8: "https://imgur.com/iTWuoIU.jpg",
#     9: "https://imgur.com/jzy7shE.jpg",
#     10: "https://imgur.com/y95d5Rb.jpg",
#     11: "https://imgur.com/KMt0vV0.jpg",
#     12: "https://imgur.com/z63oxxf.jpg",
#     13: "https://imgur.com/U86lFJk.jpg",
#     14: "https://imgur.com/PIFIWCL.jpg",
#     15: "https://imgur.com/3s8yCHu.jpg",
#     16: "https://imgur.com/BjcObqE.jpg",
#     17: "https://imgur.com/hvUIe6p.jpg"
# }

end_point = "https://ebad-1-164-249-239.ngrok-free.app"

image_dict = {
    0: f"{end_point}/face_rank/A0.jpg",
    1: f"{end_point}/face_rank/A1.jpg",
    2: f"{end_point}/face_rank/A2.jpg",
    3: f"{end_point}/face_rank/A3.jpg",
    4: f"{end_point}/face_rank/A4.jpg",
    5: f"{end_point}/face_rank/A5.jpg",
    6: f"{end_point}/face_rank/A6.jpg",
    7: f"{end_point}/face_rank/A7.jpg",
    8: f"{end_point}/face_rank/A8.jpg",
    9: f"{end_point}/face_rank/A9.jpg",
    11: f"{end_point}/face_rank/A11.jpg",
    10: f"{end_point}/face_rank/A10.jpg",
    12: f"{end_point}/face_rank/A12.jpg",
    13: f"{end_point}/face_rank/A13.jpg",
    14: f"{end_point}/face_rank/A14.jpg",
    15: f"{end_point}/face_rank/A15.jpg",
    16: f"{end_point}/face_rank/A16.jpg",
    17: f"{end_point}/face_rank/A17.jpg",
}


product_url_dict = {
    0: "https://www.cosme.net.tw/products/87330/reviews",
    1: "https://www.cosme.net.tw/products/4989/reviews",
    2: "https://www.cosme.net.tw/products/85513/reviews",
    3: "https://www.cosme.net.tw/products/79415/reviews/",
    4: "https://www.cosme.net.tw/products/40527/reviews",
    5: "https://www.cosme.net.tw/products/19398/reviews",
    6: "https://www.cosme.net.tw/products/79637/reviews",
    7: "https://www.cosme.net.tw/products/90191/reviews",
    8: "https://www.cosme.net.tw/products/105363/reviews",
    9: "https://www.cosme.net.tw/products/57958/reviews",
    10: "https://www.cosme.net.tw/products/67787/reviews",
    11: "https://www.cosme.net.tw/products/58118/reviews",
    12: "https://www.cosme.net.tw/products/89784/reviews",
    13: "https://www.cosme.net.tw/products/67788/reviews",
    14: "https://www.cosme.net.tw/products/36729/reviews",
    15: "https://www.cosme.net.tw/products/82073/reviews",
    16: "https://www.cosme.net.tw/products/82072/reviews",
    17: "https://www.cosme.net.tw/products/82074/reviews",
}


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
