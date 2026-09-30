from flask import Flask, jsonify, request
 
app = Flask(__name__)
 
server_cache = {"value": 0}
 
BIT_LENGTH = 8
 
PASSWORD = "1556"  # CHANGE FOR THE PASSWORD IN HTTP TRANSMITTER. Use HEADERS (WITHOUT THE #):
# Password: 1234
 
 
@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        password = request.headers.get("Password")
        if password != PASSWORD:
            return jsonify(
                {"error": "Unauthorized. Invalid or missing password."}), 401
 
        binary_value = request.form.get("value")
        if binary_value and len(binary_value) == BIT_LENGTH and all(
                c in "01" for c in binary_value):
            server_cache["value"] = int(binary_value, 2)
            return jsonify(
                {"value": format(server_cache["value"],
                                 f'0{BIT_LENGTH}b')}), 200
 
        return jsonify({
            "error":
            f"Invalid binary value. Must be {BIT_LENGTH} bits of 0s and 1s."
        }), 400
 
    elif request.method == "GET":
        return jsonify(
            {"value": format(server_cache["value"], f'0{BIT_LENGTH}b')}), 200
 
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
 
