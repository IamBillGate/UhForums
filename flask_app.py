from flask import Flask, render_template, request, session
import sqlite3

app = Flask(__name__)
app.secret_key = ''

@app.route('/')
def main():
	return "BLANK SITE"