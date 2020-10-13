# Clyde 'Thluffy' Sinclair
# SoftDev -- Rona Ed.
# Oct 2020 

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

#No hablo queso in the top left corner, prints "about to print __name__..."
#and then on the next line __name__ equal to the number of times someone
#goes to that website (including refreshes)
#debug mode gets turned on only if this file isn't imported
#(so it should be enabled)

#exactly as expected
