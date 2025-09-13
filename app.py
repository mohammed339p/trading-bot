from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if not data:
        return jsonify({"status": "error", "message": "no data"}), 400

    # استقبال بيانات الصفقة من TradingView
    symbol = data.get("symbol")
    price = data.get("price")
    stop = data.get("stop")
    target1 = data.get("target1")
    target2 = data.get("target2")

    print("📩 إشارة جديدة من TradingView")
    print(f"الزوج: {symbol}")
    print(f"سعر الدخول: {price}")
    print(f"ستوب لوز: {stop}")
    print(f"هدف 1: {target1}")
    print(f"هدف 2: {target2}")

    return jsonify({"status": "success", "message": "Webhook received"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)