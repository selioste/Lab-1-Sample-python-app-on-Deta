from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def app(event):
    prefix_google = """
     <!-- Google tag (gtag.js) -->
    <script async 
    src="https://www.googletagmanager.com/gtag/js?id=UA-250915546-1"></script>
    <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'UA-250915546-1');
    </script>
     """
    return prefix_google + "Hello, world!"