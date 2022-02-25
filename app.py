import requests
from bs4 import BeautifulSoup


def url() -> str:
    return "".join({
        "origin": "https://finance.naver.com",
        "iframe": "/marketindex/exchangeDailyQuote.naver",
        "query": "?marketindexCd=FX_EURKRW"
    }.values())


def user_agent() -> str:
    return " ".join([
        "Mozilla/5.0",
        "(Windows NT 10.0; Win64; x64)",
        "AppleWebKit/537.36,"
        "(KHTML, like Gecko)",
        "Chrome/73.0.3683.86",
        "Safari/537.36"
    ])


def crawling() -> any:
    headers = {'User-Agent': user_agent()}
    data = requests.get(url(), headers=headers).text
    soup = BeautifulSoup(data, 'html.parser')

    selectors = {
        "trs": "div > table > tbody > tr",
        "date": "td:nth-child(1)",
        "rate": "td:nth-child(2)"
    }

    trs = soup.select(selectors["trs"])

    for tr in trs:
        date = tr.select_one(selectors["date"]).text
        rate = tr.select_one(selectors["rate"]).text
        print(f"날짜: {date}\t\t기준환율: {rate}")


if __name__ == "__main__":
    crawling()
