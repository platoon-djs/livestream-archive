from flask import Flask, request, render_template

import sys, os

class Stream:
	name = ""
	filepath = ""

# Global variables
app = Flask(__name__)
basedir = "/var/www/static/streams"

# Index page
@app.route('/')
def my_index():
	folders = os.listdir (basedir) # get all files' and folders' names in the current directory
	streams = []
	for folder in folders: # loop through all the files and folders
		folderPath = os.path.join(os.path.abspath(basedir), folder)
		if os.path.isdir(folderPath): # check whether the current object is a folder or not
			files = os.listdir(folderPath)
			for file in files:
				if file.endswith(".mp4"):
					stream = Stream()
					stream.name = folder.replace("_", " ")
					stream.filepath = 'static/streams/' + folder + '/' + file
					streams.append(stream)
	return render_template('index.html', streams=streams)

# Server start
if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5002)


