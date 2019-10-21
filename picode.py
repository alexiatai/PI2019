from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")

def pagina_web():
    return render_template("pi2019.html")
@login_required

app.run()
