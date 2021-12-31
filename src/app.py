from factory import create_app

app = create_app()


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(
        debug=True,
        use_reloader=True,
        host=app.config["APP_HOST"],
        port=app.config["APP_PORT"]
    )
