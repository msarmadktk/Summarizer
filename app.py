from flask import Flask, render_template, request
import summarize

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        article = request.form["article"]
        num_sentences = int(request.form["num_sentences"])
        algorithm = request.form["algorithm"]
        summary = summarize.summarize_text(article, num_sentences=num_sentences, algorithm=algorithm)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
