from pymongo import MongoClient


# Requisito 10
def top_5_news():
    with MongoClient() as client:
        db = client.tech_news
        news_list = db.news.aggregate([
                {
                    "$addFields": {
                        "popularity": {
                            "$sum": ["$shares_count", "$comments_count"]
                        }
                    }
                },
                {"$sort": {"popularity": -1, "title": 1}},
                {"$limit": 5}
            ])
    return ([(news_item["title"],
            news_item["url"]) for news_item in news_list])


# Requisito 11
def top_5_categories():
    with MongoClient() as client:
        db = client.tech_news
        news_list = db.news.aggregate([
                {
                    "$addFields": {
                        "popularity": {
                            "$sum": ["$shares_count", "$comments_count"]
                        }
                    }
                },
                {"$sort": {"popularity": -1, "title": 1}},
                {"$limit": 5}
            ])
    return ([(news_item["title"],
            news_item["url"]) for news_item in news_list])
