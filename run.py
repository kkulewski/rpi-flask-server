from flask import Flask
app = Flask(__name__)
import os
import subprocess

@app.route("/")
def hello():
    return "Hello!<br>address/r/ == read file<br>address/w/variable == write variable to file"

@app.route("/r/")
def read():
	file = open("file.txt", "r")
	data = file.read()
	file.close()
	return "%s" % data
	
@app.route("/w/<variable>")
def write(variable):
	cmd = "sudo echo %s\<br\> >> file.txt" % variable
	os.system(cmd)
	os.system("new value written to file")
	return "value [ %s ] saved to file" % variable
	
#@app.route("/f/")
#def filelist():
#	cmd = "ls"
#	data = subprocess.check_output(cmd)
#	return "%s" % data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
