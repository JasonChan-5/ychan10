# Clyde 'Thluffy' Sinclair
# SoftDev -- Rona Ed.
# Oct 2020 

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()

#No hablo queso in the top left corner, prints "about to print __name__..."
#and then on the next line __name__ equal to the number of times someone
#goes to that website (including refreshes)
#debug mode gets turned on, not too sure what it will do
#maybe we have to run hello_world by ourselves

#exactly as expected
#debug is active, and a pin came up. The webpage also restarted it seems (with stat)
#Accidently touched the file while the webpage was running, and saved, and
#it restarted the server
