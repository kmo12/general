import requests
import json
from urllib.parse import urlparse


def get_yandex_company_reviews(company_id: int, page: int = 1, min_rating: int = 4) -> list:
    url_post = "https://yandex.ru/maps/api/business/fetchReviews"

    url = url_post + "?ajax=1" + \
          f"&businessId={company_id}" + \
          "&csrfToken=97fd195e6cf78eb6f395d7c395d296ab5c11d1f1:1571717475" + \
          f"&page={page}" + "&pageSize=7" + \
          "&ranking=by_time" + \
          "&reqId=1571655534207434-3187132131-sas1-1604&sessionId=1571655349968_626529"

    s = requests.session()
    p = s.post(url_post)

    data = json.loads(p.content)

    parsed = urlparse(url)
    querys = parsed.query.split("&")
    querys[2] = "csrfToken" + "=" + data['csrfToken']
    querys = "&".join(querys)

    url = url_post + "?" + querys

    r = s.get(url)

    result = json.loads(r.content)

    raw_reviews_list = result['data']['reviews']

    for index, review in enumerate(raw_reviews_list):
        if review['rating'] < min_rating:
            del raw_reviews_list[index]
            continue
        del review['reviewId']
        del review['author']['avatarUrl']
        # Делаем дату и время из '2020-05-12T09:36:50.239Z' -> ['09:36:50', '12-05-2020']
        updated_time = review['updatedTime'].split("T")
        updated_time[0] = updated_time[0].split("-")
        updated_time[0][0], updated_time[0][1], updated_time[0][2] = updated_time[0][2], updated_time[0][1], updated_time[0][0]
        updated_time[0] = "-".join(updated_time[0])
        updated_time = [updated_time[1][:8], updated_time[0]]
        review['updatedTime'] = updated_time

    return raw_reviews_list



