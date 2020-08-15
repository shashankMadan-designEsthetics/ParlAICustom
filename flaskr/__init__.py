import os

from flask import Flask, render_template, request
from parlai.agents.tfidf_retriever.actor import TfidfRetrieverActor

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/login/', methods=["GET", "POST"])
    def login_page():
        error = ''
        try:
            print('request.method', request.method)
            if request.method == "POST":
                attempted_username = request.form['username']
                attempted_password = request.form['password']
                # flash(attempted_username)
                # flash(attempted_password)
                app.logger.info('testing info log')

                if attempted_username == "admin" and attempted_password == "password":
                    return "Your In Bitch!"

                else:
                    error = "Invalid credentials. Try Again."

            return render_template("./login.html", error=error)

        except Exception as e:
            # flash(e)
            return render_template("login.html", error=error)

    # allow both GET and POST requests
    @app.route('/form-example', methods=['GET', 'POST'])
    def form_example():
        if request.method == 'POST':  # this block is only entered when the form is submitted
            language = request.form.get('language')
            framework = request.form['framework']

            actor = TfidfRetrieverActor()
            reply = actor.run_actor()

            return '''<h1>The language value is: {}</h1>'''.format(reply)

        return '''<form method="POST">
                    Language: <input type="text" name="language"><br>
                    Framework: <input type="text" name="framework"><br>
                    <input type="submit" value="Submit"><br>
                </form>'''

    return app
