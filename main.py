# A Flask app with search bar
from flask import Flask, render_template, request, render_template_string

app = Flask(__name__)
@app.route('/')
def index():
    if request.args.get('name'):
        payload = render_template_string(request.args.get('name'))
        return render_template('info.html', name=payload)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)