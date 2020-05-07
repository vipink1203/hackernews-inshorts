from flask import Flask, render_template, url_for, redirect
from scapper import create_hn
import pathlib
import os

app = Flask(__name__)


@app.route('/')
def index():
    data = create_hn()
    return render_template('index.html', data=data)


@app.route('/reload')
def reload():
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
