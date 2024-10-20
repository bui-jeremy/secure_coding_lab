from flask import Flask, request, make_response

app = Flask(__name__)

# Insecure Code Example
# The session cookie is not protected, which makes it vulnerable to theft.
# Exploit the vulnerability by examining the cookie in the browser or using a tool like Burp Suite.
@app.route('/')
def set_cookie():
    resp = make_response("Setting an insecure session cookie...")
    resp.set_cookie('session_id', '123456')
    return resp

# Secure Code Example (commented out)
# Use HTTPOnly and Secure flags on cookies to protect them from client-side access and transmission over HTTP.
'''
@app.route('/secure')
def set_secure_cookie():
    resp = make_response("Setting a secure session cookie...")
    resp.set_cookie('session_id', '123456', httponly=True, secure=True)
    return resp
'''

if __name__ == "__main__":
    app.run(debug=True)
