import streamlit as st
import time
# 定義產品資料

# 網頁配置設定(要寫在所有 Streamlit 命令之前，而且只能設定一次)
# st.set_page_config(
#     page_title="自定義網頁標題",
#     page_icon="random",
#     layout="centered",
#     initial_sidebar_state="collapsed",
# )


# 設定頁面寬度
st.set_page_config(layout="wide")

products_data = [
    {
        "photo_url": "111.jpg",
        "brand": "Brand1",
        "name": "Product1",
        "rating": 4.5,
        "tags": ["Tag1", "Tag2"],
    },
    # 依此類推，總共18項產品
]

products_data[0]["brand"] = "FOMA"


# bar = st.progress(1)
# for i in range(3):
#     bar.progress(i + 1, f'目前進度 {i+1} %')
#     time.sleep(0.05)

# bar.progress(100, '載入完成！')

# 顯示標題
st.title("洗面乳推薦系統")

# 顯示標題
st.title("產品展示")

# 顯示每項產品的資訊
for product in products_data:
    # 使用 beta_columns 將文本顯示在圖片旁邊
    col1, col2 = st.columns([1, 2])
    
    # 調整圖片大小
    col1.image(
        product["photo_url"],
        caption=f"{product['brand']} - {product['name']}",
        # use_column_width=True,
        width=200,  # 設定圖片寬度為300像素
        # height=300,  # 設定圖片高度為300像素
    )
    
    col2.write(f"**品牌:** {product['brand']}")
    col2.write(f"**產品名稱:** {product['name']}")
    col2.write(f"**星數:** {product['rating']}")
    col2.write(f"**標籤:** {', '.join(product['tags'])}")
    st.write("---")  # 分隔每項產品