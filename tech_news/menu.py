import sys
from tech_news.scraper import (
    get_tech_news
)
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


# Requisito 12
def analyzer_menu():
    options_message_output = {
        "0": ("Digite quantas notícias serão buscadas:", get_tech_news),
        "1": ("Digite o título:", search_by_title),
        "2": ("Digite a data no formato aaaa-mm-dd:", search_by_date),
        "3": ("Digite a fonte:", search_by_source),
        "4": ("Digite a categoria:", search_by_category),
        "5": ("Listar top 5 noticias", top_5_news),
        "6": ("Listar top 6 categorias", top_5_categories),
        "7": "Encerrando script"
    }
    print("""
Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.""")

    number_option = input()
    try:
        number_option = int(number_option)
        number_option = str(number_option)
        if number_option == "5" or number_option == "6":
            print(options_message_output[number_option][1]())
            return
        elif number_option == "7":
            print(options_message_output[number_option])
            return
        value = input(options_message_output[number_option][0])
        print(options_message_output[number_option][1](value))
        return
    except (ValueError, KeyError):
        print("Opção inválida", file=sys.stderr)
        return
