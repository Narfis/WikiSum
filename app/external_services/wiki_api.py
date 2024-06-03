import requests
from datetime import datetime


class WikiApi:
    def get_wiki_page(self, page_name: str):
        params = {
            "action": "query",
            "format": "json",
            "titles": page_name,
            "prop": "extracts"
        }
        response = requests.get("https://en.wikipedia.org/w/api.php?", params=params).json()
        
        key = list(response.get("query").get("pages").keys())[0]
        if key == "-1":
            return None, ""

        data = response.get("query").get("pages").get(key).get("extract")
        if "\nNewPP" in data:
            return None, ""
        
        return key, data
    
    def get_last_changes(self, page_id:int, number_of_changes:int=5):
        params = {
            "action": "query",
            "format": "json",
            "pageids": page_id,
            "prop": "revisions",
            "rvprop": "timestamp",
            "rvlimit": number_of_changes
        }

        response = requests.get("https://en.wikipedia.org/w/api.php?", params=params).json()
        
        pages = response.get("query").get("pages")
        page = list(pages.values())[0]
        revisions = page.get("revisions")

        all_dates = []

        for revision in revisions:
            timestamp_string = revision.get("timestamp")
            time_stamp = datetime.strptime(timestamp_string, "%Y-%m-%dT%H:%M:%SZ")
            normal_date_format = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
            all_dates.append(normal_date_format)

        return all_dates
