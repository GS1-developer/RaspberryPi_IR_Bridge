from flask import Flask, render_template
import datetime
import subprocess
app = Flask( __name__ )

@app .route( "/" )
def index():
    return "Test page"
    return "&lt;html&gt;&lt;body&gt;&lt;h1&gt;This is my Site (Flask)&lt;/h1&gt;&lt;/body&gt;&lt;/html&gt;"

@app.route("/Test01")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'RaspberryPi',
      'time': timeString
      }
   return render_template('myTemplate03.html', **templateData)

@app.route("/PioneerPi")
def pioneerpi():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'PionnerPi',
      'time': timeString
      }
   return render_template('myTemplate03.html', **templateData)

@app.route("/<DeviceName>")
def action(DeviceName):
   return DeviceName


@app.route("/Info")
def getInfo():
   command = ['systemctl','status','raspotify']
   result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
   result = subprocess.run(command, stdout=subprocess.PIPE)
   return result.stdout

 
if __name__ == "__main__" :
    app.run( host = '0.0.0.0' , debug = True )

