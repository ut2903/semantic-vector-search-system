from flask import Flask, request, jsonify
from core.search import entity_search
from config.paths import API_HOST, API_PORT

app = Flask("Semantic Vector Search API")

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query", "")
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    try:
        results = entity_search(query)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host=API_HOST, port=API_PORT)
