
from flask import Flask, jsonify, request
import qrcode

app = Flask(__name__)

@app.route('/qr', methods=['GET'])
def qr_code():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL parameter is required'})
    
    img = qrcode.make(url)
    response = app.response_class(
        response=img.getvalue(),
        status=200,
        mimetype='image/png'
    )
    return response

if __name__ == '__main__':
    app.run()
    