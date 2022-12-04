def app(event):
 prefix_google = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-8XGX24827F"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-8XGX24827F');
</script>
 """
 return prefix_google + "Hello World"

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def app(event):
    return "Hello, world!"