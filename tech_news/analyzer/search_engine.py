from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news_item["title"], news_item["url"]) for news_item in news_list]


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    news_list = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    return [(news_item["title"], news_item["url"]) for news_item in news_list]


# Requisito 8
def search_by_source(source):
    news_list = search_news({"sources": {"$regex": source, "$options": "i"}})
    return [(news_item["title"], news_item["url"]) for news_item in news_list]


# Requisito 9
def search_by_category(category):
    news_list = search_news({"categories": {"$regex": category, "$options": "i"}})
    return [(news_item["title"], news_item["url"]) for news_item in news_list]
