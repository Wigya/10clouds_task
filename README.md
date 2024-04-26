# 10clouds_task
The application runs on port 8080
## Setting Up and Running the Project
1. Clone the repository to your local machine:</br>
``git clone https://github.com/Wigya/10clouds_task.git``
2. Navigate to the project directory:</br>
``cd 10clouds_task``
3. Install dependencies:</br>
``pip install -r requirements.txt``
4. Add an .env file with the following fields `API_KEY` and `USERNAME`
5. Run the application(use ``python3`` if needed)</br>
``python app.py``

## Interacting with the API

### Endpoints:
* \`<b>GET `/search`</b>\`: Get list of repositories

#### Query Parameters
* `query`: The search query. Example `/search?query=Example`
* `page` (optional): The page number for paginated results. Default: `1`. Example: `/search?query=Example&page=2`
* `per_page` (optional): The number of results per page. Default: `100` Example: `/search?query=Example&per_page=20`
* `sort` (optional): Sorts the results of your query by number of `stars`, `forks`, or `help-wanted-issues` or how recently the items were `updated`. Example: `/search?query=Example&sort=stars`
* `order` (optional): Determines whether the first search result returned is the highest number of matches (`desc`) or lowest number of matches (`asc`). Default: `desc`. Example: `/search?query=Example&sort=stars&order=desc`

#### Response
<b>Successful response</b></br>
* `status`: int
* `count`: int
* `items`: { `repo_name`: string, `owner_login`: string, `repo_url`: string }</br>

<b>Unsuccessful response</b></br>
* `status`: int
* `error`: string

## Example requests you can execute
* `/search?query=Example`
* `/search?query=openAI&sort=stars`
* `/search?query=commaai&sort=forks&order=asc`


