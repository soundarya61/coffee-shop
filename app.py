from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# ---------- DATABASE CONFIG ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "users.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ---------- HOME ----------
@app.route("/")
def home():
    return render_template("index.html")
# ---------- FEEDBACK FORM ----------
@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        feedback_text = request.form.get("feedback")

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)",
            (name, email, feedback_text)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("view_feedback"))

    return render_template("form-validation.html")

# ---------- VIEW FEEDBACK ----------
@app.route("/view-feedback")
def view_feedback():
    conn = get_db_connection()
    feedbacks = conn.execute("SELECT * FROM feedback").fetchall()
    conn.close()
    return render_template("users.html", users=feedbacks)

# ---------- DELETE FEEDBACK ----------
@app.route("/delete/<int:id>")
def delete_feedback(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM feedback WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("view_feedback"))

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)

#cd frontend-project
#python app.py