import streamlit as st
from select_tool_v2 import select_1
# 定義產品資料

# This code is different for each deployed app.
# CURRENT_THEME = "blue"
# IS_DARK_THEME = True
# EXPANDER_TEXT = """
#     This is a custom theme. You can enable it by copying the following code
#     to `.streamlit/config.toml`:

#     ```python
#     [theme]
#     primaryColor = "#E694FF"
#     backgroundColor = "#00172B"
#     secondaryBackgroundColor = "#0083B8"
#     textColor = "#C6CDD4"
#     font = "sans-serif"
#     ```
#     """


# with st.chat_message("user"):  # 或者寫 "human"
#     st.write("Hi 👋，請問你是誰？")

# # 另一種寫法
# message = st.chat_message("assistant")  # 或者寫 "ai"
# # message = st.chat_message("assistant", avatar="🦖")  # 自訂頭像
# message.write("你好！我是 ChatBot 🤖，可以回答各種問題，提供資訊。")
# message.write("有什麼我可以幫助你的嗎？")

# st.chat_input("Say something...")


# 網頁配置設定(要寫在所有 Streamlit 命令之前，而且只能設定一次)
st.set_page_config(
    page_title="洗面乳推薦系統_Web",
    # page_icon="random",
    layout="centered",
    # initial_sidebar_state="collapsed",
)


gif_url = "https://media.giphy.com/media/oAjjyaboWN8h2xyPGF/giphy.gif"
st.image(gif_url, caption="洗面乳推薦系統", use_column_width=True)

# bar = st.progress(1)
# for i in range(3):
#     bar.progress(i + 1, f'目前進度 {i+1} %')
#     time.sleep(0.05)
# bar.progress(100, '載入完成！')


mark = {
        0: "FOAM", 1: "上山採藥", 2: "肌研", 3: "肌研", 4: "肌研",
        5: "莎娜", 6: "露姬婷", 7: "清妍", 8: "專科", 9: "高絲",
        10: "Biore", 11: "Biore", 12: "Bifesta", 13: "Biore", 14: "露姬婷",
        15: "Bifesta", 16: "Bifesta", 17: "Bifesta"
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

image_dict = {
    0: "https://storage.googleapis.com/aiface/Q/0.jpg",
    1: "https://storage.googleapis.com/aiface/Q/1.jpg",
    2: "https://storage.googleapis.com/aiface/Q/2.jpg",
    3: "https://storage.googleapis.com/aiface/Q/3.jpg",
    4: "https://storage.googleapis.com/aiface/Q/4.jpg",
    5: "https://storage.googleapis.com/aiface/Q/5.jpg",
    6: "https://storage.googleapis.com/aiface/Q/6.jpg",
    7: "https://storage.googleapis.com/aiface/Q/7.jpg",
    8: "https://storage.googleapis.com/aiface/Q/8.jpg",
    9: "https://storage.googleapis.com/aiface/Q/9.jpg",
    10: "https://storage.googleapis.com/aiface/Q/10.jpg",
    11: "https://storage.googleapis.com/aiface/Q/11.jpg",
    12: "https://storage.googleapis.com/aiface/Q/12.jpg",
    13: "https://storage.googleapis.com/aiface/Q/13.jpg",
    14: "https://storage.googleapis.com/aiface/Q/14.jpg",
    15: "https://storage.googleapis.com/aiface/Q/15.jpg",
    16: "https://storage.googleapis.com/aiface/Q/16.jpg",
    17: "https://storage.googleapis.com/aiface/Q/17.jpg"
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

st.markdown('<br>' * 3, unsafe_allow_html=True)




# 顯示每項產品的資訊
for i in range(18):  # 修改範圍為18
    sql_material = select_1(i)  # 總資料庫，根據迴圈i值取得對應的資料

    product_data = {
        "photo_url": image_dict[i],
        "brand": mark[i],
        "name": sql_material[1],  # 資料庫第1個欄位
        "rating": sql_material[2],  # 資料庫第2個欄位
        "tags": sql_material[3],  # 資料庫第3個欄位
        "Comment": product_url_dict[i],
    }

    # 使用 columns 將文本顯示在圖片旁邊
    col1, col2 = st.columns([1, 2])

    col1.image(
        product_data["photo_url"],
        use_column_width=False,  # 不使用欄位寬度
        width=200,  # 設定圖片寬度為200像素
    )

    col2.write(f"**品牌:** {product_data['brand']}", unsafe_allow_html=True)
    col2.write(f"**產品名稱:** {product_data['name']}", unsafe_allow_html=True)
    col2.write(f"**星數:** {product_data['rating']}", unsafe_allow_html=True)
    col2.write(f"**效果:** {product_data['tags']}", unsafe_allow_html=True)
    col2.markdown(f" [**更多評論**]({product_data['Comment']})", unsafe_allow_html=True)

    st.markdown("---")  # 分隔每項產品
