from flask import Flask
app = Flask(__name__)
import os
import subprocess

@app.route("/")
def hello():
    return "Hello!<br>address/r/ == read file"

@app.route("/r/")
def read():
	file = open("file.txt", "r")
	data = file.read()
	file.close()
	return "%s" % data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
