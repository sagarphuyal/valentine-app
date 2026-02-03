from flask import Flask, render_template
import os  # ← add this import

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's PORT, fallback to 5000 for local
    app.run(host="0.0.0.0", port=port, debug=False)  # ← critical changes here
