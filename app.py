from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h2>HTML Images</h2>"
            "<p>HTML images are defined with the img tag:</p>"

            "<img src="C:\Users\Pratik Regal\Desktop\bournvita.png" alt="W3Schools.com" width="104" height="142">"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
