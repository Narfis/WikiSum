# WikiSum
WikiSum is an API build with FastAPI to summarise and highlight key points of wikipedia articles with ChatGPT.

#Endpoints
* /wiki_page/summary/{page_name} - A summerised text based on a Wikipedia article.
* /wiki_page/key_points/{page_name} - Top five key points of a Wikipedia article.
* /wiki_page/stats/{page_name} - Some additional information such as top 10 most used words in the article, and the arcitles mean word length.
FastAPI documentation can be found at /docs.

#Setup
* pip install -r requirements.txt
* .env config
  - OPENAI_API_KEY * Required
  - DB_HOST        * Optional
  - DB_NAME        * Optional
  - DB_PASS        * Optional
  - DB_PORT        * Optional
  - DB_URL         * Optional
  - DB_USER        * Optional
* uvicorn app.main:app --host 0.0.0.0 --port $PORT

#Website
The API can be found at: https://wikisum.up.railway.app/docs 
