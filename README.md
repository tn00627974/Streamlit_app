這是一個使用Python來達到一個網頁的小型專案開發 : 

●步驟需先安裝指令 
pip install streamlit

●你需要在terminal上執行streamlit run <py程式檔案路徑>
streamlit run streamlit_app

備註 : 網頁的內容資料是由透過我們資料庫做連線,內容可能會有錯誤 (因為我們的資料庫並不公開,請填入您的資料庫streamlit.toml裡)
可查閱官方文件 https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management

your-LOCAL-repository/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml # Make sure to gitignore this!
├── your_app.py
└── requirements.txt


用streamlit開發一個快速檢視網頁 : 
!!![image](https://github.com/tn00627974/streamlit_app/assets/139155210/ed00beb4-6408-46f5-b286-20317dea51a3)
