import requests
import time
import parsel
import re
from tech_news.database import create_news

# Requisito 1


def fetch(url):
    try:
        response = requests.get(url, timeout=2)
    except requests.ReadTimeout:
        return None
    time.sleep(1)
    if response.status_code != 200:
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    if html_content is None:
        return []
    selector = parsel.Selector(html_content)
    return selector.css(
        "div.tec--list__item a.tec--card__thumb__link::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    link_next_page = selector.css("a.tec--btn::attr(href)").get()
    if link_next_page is None:
        return None
    return link_next_page


# Requisito 4
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.tec--article__header__title::text").get()
    timestamp = selector.css("time::attr(datetime)").get()
    writer = selector.css(
        ".tec--author__info *:first-child *::text").get() or selector.css(
            ".tec--timestamp__item.z--font-bold a::text").get()
    shares_count = selector.css("div.tec--toolbar__item").get()
    if shares_count is None:
        qty_shares = 0
    else:

        select_shares_text = re.search(r"\d+ Compartilharam", shares_count)
        try:
            qty_shares = re.search(
                r"\d+", select_shares_text[0])[0]
        except TypeError:
            qty_shares = 0

    coments_count = selector.css("#js-comments-btn::text").re_first(r"\d+")

    sources = selector.css(".z--mb-16 a::text").getall()

    sources = [source.strip() for source in sources]

    summary = "".join(selector.css(
        ".tec--article__body > p:first-child *::text").getall())

    categories = [category.strip() for category in selector.css(
        "[id='js-categories'] > a::text").getall()]

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer.strip() if writer else writer,
        "shares_count": int(qty_shares),
        "comments_count": int(coments_count) if coments_count else 0,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


""" print(scrape_noticia(fetch(""))) """

# Requisito 5


def get_tech_news(amount):
    news = list()
    page = "https://www.tecmundo.com.br/novidades"

    while True:
        for new in scrape_novidades(fetch(page)):
            ret_dict = scrape_noticia(fetch(new))
            news.append(ret_dict)
            if len(news) >= amount:
                break
        page = scrape_next_page_link(fetch(page))
        if not page or len(news) >= amount:
            break
    create_news(news)
    return news
