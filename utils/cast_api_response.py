def cast_api_response(response):
    """
    Map through the github API response
    and cast to the desired format
    stated in requirements
    """
    transformed_data = map(lambda item: {
        "repo_name": item["name"],
        "owner_login": item["owner"]["login"],
        "repo_url": item["html_url"]
    }, response)

    return list(transformed_data)