from flask import Flask
import os
import datetime
import getpass
import subprocess
app = Flask(__name__)
@app.route('/htop')
def htop():
    username = getpass.getuser()
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    top_output = subprocess.getoutput("ps aux --sort=-%mem | head -10")
    response = f"""
    <h2>Name: Yogitha Rayapureddy</h2>
    <h2>User: {username}</h2>
    <h2>Server Time (IST): {ist_time}</h2>
    <pre>Top Output:\n{top_output}</pre>
    """
    return response
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
