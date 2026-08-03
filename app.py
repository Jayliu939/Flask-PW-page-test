from flask import Flask, render_template, request
import csv


app = Flask(__name__)

past_meeting_notes = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/new_note", methods=["GET", "POST"])
def new_note():
    if request.method == "POST":
        with open("NOTES.csv", "a") as file:
            writer = csv.writer(file)
            date = request.form.get("date")
            venue = request.form.get("venue")
            notes = request.form.get("notes")
            actions = request.form.get("actions")
            writer.writerow([date, venue, notes, actions])
            
    return render_template("new_note.html")

@app.route("/past_note", methods=["GET", "POST"])
def past_note():
    meeting_data = []
    with open("NOTES.csv", "r") as file:
        reader = csv.reader(file)
        for meeting in reader:
            if meeting == []:
                continue
            else:
                meeting_data.append(meeting)
            print(meeting)
    return render_template("notes.html",
                           meeting_data=meeting_data
                           )

@app.route("/weather", methods=["GET", "POST"])
def weather():
    return render_template("weather.html")

if __name__ == "__main__":
    app.run(port=5678)
