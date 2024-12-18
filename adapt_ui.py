# -*- coding: utf-8 -*-
"""Adapt_UI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fin3zEwQ477sO9g_UddOc8PYue2OKmJA
"""

!pip install tensorflow numpy

# Create a directory for the project
import os
os.makedirs('adaptive_theme_project', exist_ok=True)

# Write HTML content
with open('adaptive_theme_project/index.html', 'w') as f:
    f.write("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Adaptive Theme Changer</title>
        <link id="theme-style" rel="stylesheet" href="light.css">
    </head>
    <body>
        <h1>Welcome to Adaptive Theme Changer!</h1>
        <button onclick="switchTheme()">Switch Theme</button>
        <script src="theme.js"></script>
    </body>
    </html>
    """)

# Write CSS content for light mode
with open('adaptive_theme_project/light.css', 'w') as f:
    f.write("""
    body {
        background-color: white;
        color: black;
    }
    """)

# Write CSS content for dark mode
with open('adaptive_theme_project/dark.css', 'w') as f:
    f.write("""
    body {
        background-color: black;
        color: white;
    }
    """)

# Write JavaScript for theme switching
with open('adaptive_theme_project/theme.js', 'w') as f:
    f.write("""
    function switchTheme() {
        const currentTheme = document.getElementById('theme-style').getAttribute('href');
        const newTheme = currentTheme === 'light.css' ? 'dark.css' : 'light.css';
        document.getElementById('theme-style').setAttribute('href', newTheme);
    }
    """)

import numpy as np

# Simulate user behavior data
# Columns: [Time of Day (0-23), Theme Preference (0: Light, 1: Dark)]
data = np.array([
    [8, 0], [9, 0], [18, 1], [19, 1],  # Morning -> Light, Evening -> Dark
    [21, 1], [22, 1], [7, 0], [6, 0]   # Early Morning -> Light
])

# Save data for training
np.save('adaptive_theme_project/user_data.npy', data)

import tensorflow as tf

# Load the data
data = np.load('adaptive_theme_project/user_data.npy')
X, y = data[:, 0], data[:, 1]

# Normalize inputs
X = X / 23.0

# Create a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=50, verbose=0)

# Save the model
model.save('adaptive_theme_project/theme_model.keras') # Add .keras extension to the filename

!pip install tensorflowjs
!tensorflowjs_converter --input_format=tf_saved_model adaptive_theme_project/theme_model adaptive_theme_project/theme_model_js



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

# Create the Flask application file `app.py`
with open('adaptive_theme_project/app.py', 'w') as f:
    f.write("""
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
    """)

!pip install Flask

!FLASK_APP=adaptive_theme_project/app.py flask run --host=0.0.0.0 --port=8000 --no-reload

!pip install flask-ngrok

from flask import Flask, render_template_string
import datetime
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # This will expose your app to the internet

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
    # Just call app.run() without additional arguments
    app.run()

!python adaptive_theme_project/app.py