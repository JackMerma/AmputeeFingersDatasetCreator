from config import *
from src.process.src import *
from src.gui.main import *
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")
    """
    # Getting parser
    args = load_parser()

    if args.process:
        process(src_type=args.type, file_path=args.file)
    else: # No args loads the user interface
        gui()
    """


if __name__ == "__main__":
    app.run(debug=True)
