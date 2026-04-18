import funtions as f
from flask import Flask, jsonify

# Heroes API -- By: @dso-uniandes (Daniel M. Serna O) :)
# Just add:
# Specific Autoscaling permissions to the service role
# Specific Cloudformation permissions to the service role
# Specific EC2 permissions to the service role
# Specific Elasticbeanstalk permissions to the service role
# Specific S3 permissions to the service role
# Specific SNS permissions to the service role

application = Flask(__name__)
data = f.load_file('./heroes.csv')

@application.route("/")
def index():
    return jsonify(data)

@application.route("/<string:id>")
def heroe(id):
    return jsonify(data[id])

if __name__ == "__main__":
    application.run(port = 5000, debug = True)