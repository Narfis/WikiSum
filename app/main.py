from fastapi import FastAPI
from app.external_services.wiki_api import WikiApi
from app.external_services.chat_api import ChatAPI
from app.components.stats import Statistics
from app.components.db import DataBase
from app.schemas.fast_api_schema import Summary, KeyPoints, Stats
from uuid import uuid4

app = FastAPI()
chat_api = ChatAPI()
stats = Statistics()
wiki = WikiApi()
db = DataBase()

#api: https://en.wikipedia.org/w/api.php
@app.get("/wiki_page/summary/{page_name}", response_model=Summary)
def page_summary(page_name: str):
    
    summary_check = db.get_summary(page_name)
    if summary_check:
        return {"wiki_summary": summary_check}
    
    _, wiki_data = wiki.get_wiki_page(page_name)

    if not wiki_data:
        return {"wiki_summary": "No data found for this page."}
    
    summary = chat_api.summarise_wikipedia_post(wiki_data)
    summary_content = chat_api.get_content(summary)
    db.insert_summary(page_name, summary_content)

    return {"wiki_summary": summary_content}

@app.get("/wiki_page/key_points/{page_name}", response_model=KeyPoints)
def page_key_points(page_name: str):

    key_points_check = db.get_key_points(page_name)
    if key_points_check:
        return {"wiki_key_points": key_points_check}
    
    _, wiki_data = wiki.get_wiki_page(page_name)
    if not wiki_data:
        return {"wiki_key_points": "No data found for this page."}

    id = uuid4()
    key_points = chat_api.key_points(wiki_data)
    key_points_content = chat_api.get_content(key_points)
    key_point_list = key_points_content.split("\n")
    db.insert_key_points(page_name, key_point_list, id)

    return {"wiki_key_points": key_point_list}
    
@app.get("/wiki_page/stats/{page_name}", response_model=Stats)
def page_stats(page_name: str):
    wiki_key, wiki_data = wiki.get_wiki_page(page_name)

    if not wiki_data:
        return {"wiki_stats": "No data found for this page."}
    
    most_used_words = stats.get_most_used_words(wiki_data)
    words_list = [[word, str(count)] for word, count in most_used_words]

    last_change_date = wiki.get_last_changes(wiki_key)

    mean_word_length = stats.get_mean_word_length(wiki_data)

    return {"wiki_stats" : {"most_common_words": words_list, 
                            "mean_word_length": mean_word_length, 
                            "last_changes": last_change_date}
                            }