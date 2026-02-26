# app.py - 这是你的数据中转站

# 1. 导入必要的工具
from flask import Flask, jsonify  # Flask用于创建网站/接口
import requests                # requests用于Python去上网

# 2. 创建一个应用
app = Flask(__name__)

# 3. 定义一个路由，当有人访问 /get-seatable-data 时触发
@app.route('/get-seatable-data')
def get_data():
    # === ⚠️ 请检查这里：把你的Token填进去 ===
    BASE_TOKEN = "e631bcec-726c-4c15-8785-762bacd61147" 
    API_URL = f"https://cloud.seatable.cn/api/v2.1/dtables/{BASE_TOKEN}/rows/"
    
    # 4. Python“亲自”去请求SeaTable (这一步没有跨域限制！)
    headers = {'Authorization': 'Token ' + BASE_TOKEN}
    response = requests.get(API_URL, headers=headers)
    
    # 5. 把拿到的数据原封不动地返回给你的HTML网页
    return jsonify(response.json())

# 6. 启动服务器
if __name__ == '__main__':
    # 这会让Python在本地开启一个服务
    app.run(port=5000, debug=True)