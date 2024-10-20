from flask import Flask, request

app = Flask(__name__)

# Insecure Code Example
# This code is vulnerable to Cross-Site Scripting (XSS) because it directly displays user input.

# Try to visit: http://127.0.0.1:5000/?input=<script>alert('XSS')</script>
@app.route('/')
def home():
    user_input = request.args.get('input', '')
    return f"<h1>Welcome {user_input}!</h1>"

# Secure Code Example (commented out)
# Uncomment the code below to use the secure version with proper escaping to prevent XSS attacks.
'''
from flask import escape

@app.route('/')
def home():
    user_input = request.args.get('input', '')
    return f"<h1>Welcome {escape(user_input)}!</h1>"
'''

if __name__ == "__main__":
    app.run(debug=True)
