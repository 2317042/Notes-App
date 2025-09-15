from flask import Flask, request

app = Flask(__name__)

# Store notes in memory (simple list)
notes = []

@app.route("/")
def home():
    # Display form + list of notes
    return f"""
    <html>
    <head><title>Notes App</title></head>
    <body>
        <h2>Sticky Notes</h2>
        <form action="/add" method="post">
            <input type="text" name="note" placeholder="Enter your note" required>
            <button type="submit">Add Note</button>
        </form>
        <h3>All Notes:</h3>
        <ul>
            {''.join(f"<li>{n}</li>" for n in notes)}
        </ul>
    </body>
    </html>
    """

@app.route("/add", methods=["POST"])
def add_note():
    note = request.form.get("note", "")
    if note:
        notes.append(note)
    return home()  # Redirect to home page with updated notes

if __name__ == "__main__":
    app.run(debug=True)
