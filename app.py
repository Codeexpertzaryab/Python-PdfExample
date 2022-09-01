from distutils.command.config import config
from fileinput import filename
from flask import Flask
from flask import render_template
from flask import make_response
import pdfkit,os
app = Flask(__name__)
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

@app.route("/")
def index1():
    return render_template('check.html',name='zaryab')

@app.route("/pdf/<string:name>")
def index(name):
    html = render_template('download.html',name=name)
    pdf = pdfkit.from_string(html,False, configuration=config)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = 'inline'; 'filename='+name+'.pdf'
    return response


if __name__ == "__main__":
    app.run(debug=True)