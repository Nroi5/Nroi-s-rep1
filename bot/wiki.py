#wiki.py
import wikipedia #pip install wikipedia

def get_info_wiki(article):
    wikipedia.set_lang("ru") #установил язык

    try:
        return f"{wikipedia.summary(article)}" # запрос на получение статьи и ссылки
    except wikipedia.WikipediaException: #если ошибка (статья не найдена)
        return "Информация не найдена"

