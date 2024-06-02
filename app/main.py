from fastapi import FastAPI
from app.external_services.media_wiki import get_wiki_page
from app.external_services.chat_gpt import ChatGPT
from app.components.stats import Statistics

app = FastAPI()
chat_gpt = ChatGPT()
stats = Statistics()

def get_content(gpt_data: dict):
    choice = dict(gpt_data).get("choices")[0]
    message = dict(choice).get("message")
    content = dict(message).get("content")
    return content

#api: https://en.wikipedia.org/w/api.php
@app.get("/wiki_page/summary/{page_name}")
def page_summary(page_name: str):
    wiki_data = get_wiki_page(page_name)

    if not wiki_data:
        return {"wiki_summary": "No data found for this page."}
    
    summary = chat_gpt.summarise_wikipedia_post(wiki_data)

    summary_content = get_content(summary)

    return {"wiki_summary": summary_content}

@app.get("/wiki_page/key_points/{page_name}")
def page_key_points(page_name: str):
    wiki_data = get_wiki_page(page_name)

    if not wiki_data:
        return {"wiki_summary": "No data found for this page."}
    
    key_points = chat_gpt.key_points(wiki_data)

    key_points_content = get_content(key_points)

    key_point_list = key_points_content.split("\n")

    return {"wiki_summary": key_point_list}
    
@app.get("/wiki_page/stats/{page_name}")
def page_stats(page_name: str):
    wiki_data = get_wiki_page(page_name)

    if not wiki_data:
        return {"wiki_summary": "No data found for this page."}
    
    most_used_words = stats.get_most_used_words(wiki_data)
    words_list = [{"word": word, "count": count} for word, count in most_used_words]

    return {"wiki_summary" : {"most_used_words": words_list}}