from flask import Flask

app = Flask(__name__)


@app.route('/users')
def get_users():

    return {"last_name":"alla",
              "first_name":"ismail",
               "profession":"student"}

