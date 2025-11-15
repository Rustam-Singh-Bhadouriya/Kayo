from module import wikipedia  as wkp, wb
from voices import tell

def get_article(lang : str= "en", article_name: str = "Python (programming Language)"):
    wkp.set_lang(lang) # Setting Language For User (Default : english)

    try:
        Article = wkp.summary(article_name)
        # return Article
        tell(Article)
    except wkp.exceptions.DisambiguationError as e:
        print(f"Disambiguation options for '{article_name}': {e.options}")
        # return f"Disambiguation options for '{article_name}': {e.options}"
        tell("UnKnown Error")
    except wkp.exceptions.PageError:
        print("Page not found, Searching On Google")
        # return "Page not found."
        tell("Page Not Found, Searching On Google")
        search_web(article_name)


def search_web(arg : str = "Wikipedia"):
    wb.open(f"www.google.com/search?q={arg}")
    tell(f"{arg} Search On Your Default browser!")





