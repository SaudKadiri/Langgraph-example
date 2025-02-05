from langchain_community.tools.tavily_search import TavilySearchResults
import requests
def getUserDetails():
    """
    Returns the details of all the users details in json format. This is to be used for additional context.
    """
    url = "https://api.npoint.io/6078b5bb9e6b669b2bdd"
    response = requests.get(url)
    return response.json()



tools = [TavilySearchResults(max_results=1), getUserDetails]