from flask import Flask, render_template, request

import requests

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
 prefix_google = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-B42PCT518X"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-B42PCT518X');
</script>
 """
 return prefix_google + "Hello World, i am Elioste, data science student at EPF engineering school"

# Lab 2 : Test the python logger
# Define response for request
def redirect_response():
    if request.form["submit"] == "Logger":
        return redirect(url_for("logger"))
    return "Connecté!"

# Define logger on deta
@app.route('/logger')
@app.route('/logger', methods=["GET"])
def logger():
    print('Back-end logs :', file=sys.stderr)
    logging.info("Logging test")
    script = """
    <script> console.log("Login page") </script>
    """
    return render_template("logger.html") + script

if __name__ == '__main__':
    app.run(debug = True)

# Lab 2: Maniplate cookies - Request with oauth
@app.route('/cookies', methods = ['GET', 'POST'])
def get_cookies():
    req = requests.get("https://www.google.com/")

    return req.cookies.get_dict()