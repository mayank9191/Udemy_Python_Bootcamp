from flask import Flask

app = Flask(__name__)


@app.route("/")
def heallo_world():
    return '<h1 style="text-align: center;color: red">Hello World!</h1>' \
        ' <p>This is my paragraph</p>' \
        ' <img src= "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzM1ZHYzMXpmZGI0NmFpNDh2aWp2Z2ZjZm96eWlqMGtxdmEybDJqdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/PqfnfRcHzzFlGd3ENd/giphy.webp">'\
        '<img src= "https://media.giphy.com/media/nR4L10XlJcSeQ/giphy.gif?cid=790b76110dy3f2tpqxmepwquoch5vooolpdac71qhrih9lbo&ep=v1_gifs_search&rid=giphy.gif&ct=g" width=500>'
    # '<img src= "https://media.giphy.com/avatars/catgrass/fAQZ44ZCAFTy/200h.gif>'\


@app.route("/bye")
def say_bye():
    return "Goodbye!"


if __name__ == "__main__":
    app.run(debug=True)
