這是一個使用Python來達到一個網頁的小型專案開發 : 

●使用語言 : python

●需先在你的編碼器安裝以下指令 

pip install streamlit


●你需要在terminal上執行streamlit run <py程式檔案路徑> ,會彈跳出一個內部網頁可預覽

streamlit run streamlit_app


備註 : 網頁的內容資料是由透過我們資料庫做連線(因為我們的資料庫並不公開,請填入您的資料庫secrest.toml裡)
可查閱官方文件 

https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management

secrest.toml的路徑請參考以下 (記得在git push前,將secrest.toml加入在.gitignore裡) ※以免資料外洩

![image](https://github.com/tn00627974/streamlit_app/assets/139155210/4aec55cf-ffb5-4da7-a5f7-9f05a071fed7)



用streamlit開發一個快速檢視網頁 : 
!!![image](https://github.com/tn00627974/streamlit_app/assets/139155210/ed00beb4-6408-46f5-b286-20317dea51a3)
