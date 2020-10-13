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

app.run()

#No hablo queso in the top left corner, prints "about to print __name__..."
#and then on the next line __name__ equal to the number of times someone
#goes to that website (including refreshes)

#exactly as expected

