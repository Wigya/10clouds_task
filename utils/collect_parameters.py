from flask import request

def collect_parameters():
    query = request.args.get("query")
    sort = request.args.get("sort")
    order = request.args.get("order")
    page = request.args.get("page")
    per_page = request.args.get("per_page")

    return query, sort, order, page, per_page