#!/usr/bin/env python2
# coding: utf-8

import time
import subprocess

from flask import Flask
app = Flask(__name__)


template = '''
<!DOCTYPE html>
<html>
<head>
<style>
html {{
    color: #4e4e4e;
    font-size: 40pt;
    background-color: #FFFCE4;
    text-align: center;
    font-family: "Sans";
}}
ul {{
    list-style-type: none;
    padding: 0px;
}}
li {{
    padding: 20px;
}}
a {{
    text-decoration: none;
}}
.btn {{
    color: #FFFCE4;
    border-color: silver;
    border-style: solid;
    border-radius: 20px;
    padding: 5px 30px;
    background-color: #1b5298;
}}
.danger {{
    color: red;
}}
.safe {{
    color: green;
}}
</style>
<script>
function starting () {{
    document.getElementsByTagName('body')[0].innerHTML= '<p>starting...</p>'
}}
</script>
</head>
<body>
<p>sshd running: <a href="/"><span class="{status_class}">{running}</span></a></p>
<ul>
    <li><a class="btn" href="start" onclick="starting()">start</a></li>
    <li><a class="btn" href="stop">stop</a></li>
</ul>
<p>{info}</p>
</body>
</html>
'''


def sshd_running():
    '''
    Return 'yes' if SSHD is running, 'no' otherwise.
    '''
    try:
        ret = subprocess.check_output(
            ['bash', '-c', 'echo "dummy" | nc localhost 22'])
        ret = 'yes'
    except subprocess.CalledProcessError as e:
        # Netcat returned error because SSHD is off?
        ret = 'yes' if 'ssh' in e.output.lower() else 'no'
    except:
        ret = 'error in check output'
    return ret


def render_page(info=''):
    '''
    Render the HTML page. `info` can be used to display a message
    below the buttons.
    '''
    running = sshd_running()
    return template.format(
        running=running,
        status_class='danger' if running == 'yes' else 'safe',
        info=info)


@app.route("/start")
def start_sshd():
    '''
    Start SSHD and render the menu.
    '''
    try:
        ret = subprocess.Popen(
            # ['/system/xbin/su', '-c', '/system/bin/start-ssh'])
            ['su', '-c', 'start-ssh'])
    except:
        ret = 'error to start sshd'
    # Wait a few seconds to SSHD to start, so the status will be right when
    # page is rendered.
    time.sleep(3)
    return render_page(ret)


@app.route("/stop")
def stop_sshd():
    '''
    Stop SSHD and render the menu.
    '''
    try:
        ret = subprocess.check_output(
            ['su', '-c', 'bash -c "killall sshd"'])
    except:
        ret = 'error to kill sshd'
    return render_page(ret)


@app.route("/")
def main():
    '''
    Render the menu.
    '''
    return render_page()

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
