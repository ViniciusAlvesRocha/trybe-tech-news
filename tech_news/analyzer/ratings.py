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
    categories = []
    with MongoClient() as client:
        db = client.tech_news
        items_database = db.news.find({})

    for item in items_database:
        categories.extend(item["categories"])

    relation_categories = {}
    for category in categories:
        if category not in relation_categories:
            relation_categories[category] = 1
        else:
            relation_categories[category] += 1

    relation_categories = sorted(
        relation_categories,
        key=relation_categories.get)

    relation_categories.sort()
    return relation_categories[:5]
