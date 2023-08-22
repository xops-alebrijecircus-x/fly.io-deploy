import os
from flask import Flask
app = Flask(__name__)

# Place and run app.py in the same root repository as the code to deploy.
username = {{ USERNAME }}
token = {{ ACCESS_TOKEN }}
namespace = {{ RESPOSITORY }} # 

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://{{usernmae}}:{{token}}@github.com/{{namespace}}/fly.io-deploy ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 main.py &")
