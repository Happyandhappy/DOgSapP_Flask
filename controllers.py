from application import app


@app.route("/test/", methods=["GET"])
def test():
    print('test')
    return 'hi'