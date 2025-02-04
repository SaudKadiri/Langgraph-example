from langchain_community.tools.tavily_search import TavilySearchResults

def username():
    """
    Returns the current user's name
    """
    return "Saud Kadiri"


tools = [TavilySearchResults(max_results=1), username]