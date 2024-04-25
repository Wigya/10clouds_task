from flask import Flask, jsonify
import os
import requests
from requests import Response
from dotenv import load_dotenv
from utils.cast_api_response import cast_api_response
from utils.collect_parameters import collect_parameters

app = Flask(__name__)

load_dotenv()

API_KEY = os.environ.get("API_KEY")
USERNAME = os.environ.get("USERNAME")

@app.route("/search", methods=["GET"])
async def searchRepositories():
    base_url = "https://api.github.com/search/repositories"

    query, sort, order, page, per_page = collect_parameters()

    if(query is None):
        return jsonify({"error": "Missing mandatory query parameter 'query'", "status": 400}), 400

    if(query):
        base_url += f"?q={query}"
    if(sort):
        base_url += f"?sort={sort}"
    if(order):
        base_url += f"?order={order}"
    if(page):
        base_url += f"?page={page}"
    if(per_page):
        base_url += f"?per_page={per_page}"
    
    github_response: Response = requests.get(base_url, auth=(USERNAME, API_KEY))

    if(github_response.status_code == 200):
        github_response_items: list = github_response.json()["items"]
        casted_data: list = cast_api_response(github_response_items)

        return {"status": 200, "items": casted_data}, 200
    elif (github_response.status_code == 304):
        return {"status": 304, "error": "[GitHub Service] Not modified"}, 304
    elif (github_response.status_code == 422):
        return {"status": 422, "error": "[GitHub Service] Validation failed, or the endpoint has been spammed."}, 422
    elif (github_response.status_code == 503):
        return {"status": 503, "error": "[GitHub Service] Service unavailable"}, 503


if __name__ == "__main__":
    app.run(port=8080)
