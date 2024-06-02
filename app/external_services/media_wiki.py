import requests

def get_wiki_page(page_name: str):
    request = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&titles={page_name}&format=json"
    response = requests.get(request).json()
    
    first_key = list(response.get("query").get("pages").keys())[0]

    if first_key == "-1":
        return ""
    
    data = response.get("query").get("pages").get(first_key).get("extract")

    if str.__contains__(data, "\nNewPP"):
        return ""

    return data