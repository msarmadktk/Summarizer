from flask import Flask, request, render_template
import summarize  # We'll create this module for summarization

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    if request.method == 'POST':
        article = request.form['article']
        summary = summarize.summarize_text(article)
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
