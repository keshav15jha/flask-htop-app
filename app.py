import os
from datetime import datetime
import subprocess
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get the required information
    full_name = "Keshav Kumar Jha"  # Replace with your full name
    system_username = os.getlogin()  # Get the system username
    server_time = datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %Z')  # Get current time in IST
    
    # Get the 'top' command output (running processes)
    try:
        top_output = subprocess.check_output("top -n 1 -b", shell=True).decode('utf-8')
    except Exception as e:
        top_output = f"Error fetching top output: {e}"

    # Render the template and pass the values
    return render_template('htop.html', full_name=full_name, system_username=system_username, server_time=server_time, top_output=top_output)

if __name__ == '__main__':
    app.run(debug=True)
