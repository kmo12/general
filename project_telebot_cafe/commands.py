# -*- coding: utf-8 -*-

import requests
import json
from urllib.parse import urlparse


def get_yandex_company_reviews(company_id: int, page: int = 1, min_rating: int = 4) -> list:
    url_post = "https://yandex.ru/maps/api/business/fetchReviews"

    url = url_post + "?ajax=1" + \
          f"&businessId={company_id}" + \
          "&csrfToken=97fd195e6cf78eb6f395d7c395d296ab5c11d1f1:1571717475" + \
          f"&page={page}" + "&pageSize=10" + \
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
            raw_reviews_list[index] = None
            continue

    for index, review in enumerate(raw_reviews_list):
        if not review:
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

    result_list = list()
    for review in raw_reviews_list:
        if review:
            result_list.append(review)

    return result_list


def review_stars(stars: int = 0) -> str:
    if stars == 1:
        return "★☆☆☆☆"
    elif stars == 2:
        return "★★☆☆☆"
    elif stars == 3:
        return "★★★☆☆"
    elif stars == 4:
        return "★★★★☆"
    elif stars == 5:
        return "★★★★★"
    else:
        return "Без рейтинга"


def get_reviews_list_for_message(company_id: int, page: int = 1, min_rating: int = 4) -> list:
    raw_reviews = get_yandex_company_reviews(company_id, page, min_rating)
    result = list()

    for review in raw_reviews:
        if not review:
            continue
        result.append(
            f"{review['author']['name']}\n"
            f"{review['author']['professionLevel']}:\n" + \
            review_stars(review['rating']) + "\n"
            f"«{review['text']}»\n"
            f"{review['updatedTime'][1]} в {review['updatedTime'][0]}")

    return result


if __name__ == '__main__':
    pass
