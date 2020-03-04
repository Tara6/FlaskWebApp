from flask import Flask, render_template    
import scraper
import json  

app = Flask(__name__)

PS4Console = scraper.scrapePS4()

@app.route("/")
def home():
    return render_template("home.html", len=len(PS4Console), consoles=PS4Console)
    
if __name__ == "__main__":
    app.run(debug=True)
