"""
Simple flask demo
"""
import os
import socket
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/test")
def formatted():
    html = "<h3>Hellooo {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

# docker build -t myapp .
# docker run -p 4000:80 --name my-running-app myapp
# http://localhost:4000
