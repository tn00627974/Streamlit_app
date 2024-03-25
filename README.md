這是一個使用Python來達到一個網頁的小型專案開發 : 

●使用語言 : python

●需先在你的 編碼器 or terminal安裝以下指令\n

pip install streamlit


●你需要在terminal上執行streamlit run <py程式檔案路徑> ,會彈跳出一個內部網頁可預覽

streamlit run streamlit_app.py

備註 : 網頁的內容資料是由透過我們資料庫做連線(因為我們的資料庫並不公開,請填入您的資料庫secrest.toml裡)
可查閱官方文件 

https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management

secrest.toml的路徑請參考以下 (記得在git push前,將secrest.toml加入在.gitignore裡) ※以免資料外洩

![image](https://github.com/tn00627974/streamlit_app/assets/139155210/4aec55cf-ffb5-4da7-a5f7-9f05a071fed7)

功能概述：
顯示應用程式的標題和一個 GIF 圖片作為開頭。


使用 set_page_config 函數設置網頁配置，包括頁面標題和配置設定。


定義了產品資料的字典，其中包括產品的品牌、名稱、評分、標籤和更多評論的連結。


使用 image_dict 包含每個產品的圖片 URL。


使用 product_url_dict 包含每個產品的更多評論連結 URL。


透過 select_tool_v2 模組中的 select_1 函數來查詢產品資料。


透過 st.image 顯示 GIF 圖片，並使用 st.markdown 進行格式化文本的顯示。


使用迴圈遍歷產品資料，顯示每項產品的圖片、品牌、名稱、星數、效果和更多評論的連結。


使用 st.markdown("---") 在每項產品之間添加分隔線。


技術文件：
這個程式碼基於 Python 語言，使用了 Streamlit 框架來構建 Web 應用程式。你可以在 Streamlit 官方文檔 中找到有關 Streamlit 的更多資訊和教程。此外，該程式還使用了一些常用的 Python 函數和字典來處理產品資料和顯示介面。

用streamlit開發一個快速檢視網頁 : 
!!![image](https://github.com/tn00627974/streamlit_app/assets/139155210/ed00beb4-6408-46f5-b286-20317dea51a3)
