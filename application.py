import sys
from flask import Flask, request, abort, jsonify
from controllers.auth import authapi as auth

application = Flask(__name__)
application.register_blueprint(auth)

print('******************')
print(sys.path)


@application.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Page Not Found'})

# before 500 errors started happening on eb (elastic beanstalk) this route used to work fine
# because it was in the main `application.py` file
@application.route('/test/', methods=["GET"])
def test():
    return jsonify({'data': 'This is a test page'})


# If I remove this block, then **even local dev server** will not be able to access `/test-auth/`
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
