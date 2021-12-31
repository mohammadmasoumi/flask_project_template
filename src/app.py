from project import create_app

app = create_app()


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(
        debug=True,
        use_reloader=True,
        host='0.0.0.0'
    )
