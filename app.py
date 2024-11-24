
from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Get current hour
    current_hour = datetime.datetime.now().hour

    # Decide which theme to serve (light in the morning, dark in the evening)
    if 6 <= current_hour < 18:
        theme = 'light.css'  # Daytime: light theme
    else:
        theme = 'dark.css'   # Nighttime: dark theme

    # Read the HTML file as a string and inject the selected theme
    with open('adaptive_theme_project/index.html', 'r') as file:
        html_content = file.read()

    return render_template_string(html_content, theme=theme)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
    