from flaskblog import create_app

app = create_app()

# This conditional is only true if we run the script from Python directly i.e., use "python flaskblog.py" in 
# the Terminal.
if __name__ == "__main__":
    app.run(debug=True)
