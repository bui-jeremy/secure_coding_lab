from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Insecure Code Example
# This endpoint is vulnerable to CSRF because it lacks verification.
# To exploit: create a form on another site that auto-submits a POST request to this endpoint.
@app.route('/transfer', methods=['POST'])
def transfer_funds():
    amount = request.form.get('amount')
    print(f"Transferring ${amount} to another account...")
    return f"Transferred ${amount}!"

# Secure Code Example (commented out)
# Implement CSRF protection by using a hidden token to verify the user's identity.
# '''
# from flask import render_template_string
# import secrets

# @app.route('/transfer', methods=['POST'])
# def transfer_funds():
#     token = request.form.get('csrf_token')
#     if token != session.get('csrf_token'):
#         return "Invalid CSRF token", 403
#     amount = request.form.get('amount')
#     print(f"Transferring ${amount} to another account...")
#     return f"Transferred ${amount}!"

# @app.route('/form')
# def form():
#     csrf_token = secrets.token_hex(16)
#     session['csrf_token'] = csrf_token
#     return render_template_string('''
#         <form method="POST" action="/transfer">
#             <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
#             Amount: <input type="text" name="amount">
#             <input type="submit" value="Transfer">
#         </form>
#     ''', csrf_token=csrf_token)
# '''
if __name__ == "__main__":
    app.run(debug=True)
