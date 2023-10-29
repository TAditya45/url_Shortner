from flask import Flask, request, jsonify
import hashlib
import secrets

app = Flask(__name__)

url_mappings = {}
url_metadata = {}
counter = 0  # Counter for short url

def generate_short_url(long_url):
    global counter
    salt = secrets.token_hex(4)  # Generating a 4byte salt
    data = long_url.encode() + salt.encode()
    sha256_hash = hashlib.sha256(data).hexdigest()
    short_url = sha256_hash[:8] + str(counter)  # hash + counter to keep uniqueness
    counter += 1
    return short_url

@app.route('/shorten', methods=['POST'])
def create_short_url():
    data = request.get_json()
    long_url = data.get('long_url')

    if not long_url:
        return jsonify({"error": "Long URL is required"}), 400

    short_url = generate_short_url(long_url)
    url_mappings[short_url] = long_url
    url_metadata[short_url] = {"hits": 0}

    return jsonify({"short_url": short_url}), 201

@app.route('/search', methods=['GET'])
def search_urls():
    term = request.args.get('term')

    if not term:
        return jsonify({"error": "Search term is required"}), 400

    results = {}
    for short_url, long_url in url_mappings.items():
        if term.lower() in long_url.lower():
            results[short_url] = {"url": long_url, "hits": url_metadata[short_url]["hits"]}

    return jsonify(results)

@app.route('/metadata/<short_url>', methods=['GET'])
def get_metadata(short_url):
    if short_url in url_metadata:
        return jsonify(url_metadata[short_url])
    else:
        return jsonify({"error": "Short URL not found"}), 404

@app.route('/<short_url>', methods=['GET'])
def redirect_to_long_url(short_url):
    if short_url in url_mappings:
        url_metadata[short_url]["hits"] += 1
        return jsonify({"long_url": url_mappings[short_url]}), 302
    else:
        return jsonify({"error": "Short URL not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
