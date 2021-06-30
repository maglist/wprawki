import requests
import pytest


def test_cat():
    url_image = "https://ichef.bbci.co.uk/news/976/cpsprodpb/12A9B/production/_111434467_gettyimages-1143489763.jpg"
    key_words = ["cat", "animal", "mammal", "pet"]
    check_picture(url_image, key_words)

def test_people():
    url_image = "https://kidbluboo.files.wordpress.com/2016/11/office-people-images-people-in-the-office-903884-8-1.jpg"
    key_words = ["human", "apparel", "person", "suit", "accessories", "accessory", "clothing", "coat", "finger", "overcoat", "thumbs up", "tie"]
    check_picture(url_image, key_words)

def check_picture(url_image, key_words):
    url_api = "http_api_returning_JSON_with_picture_description_generated_by_AI"
    # unfortunately I am not allowed to share recognize_api URL.

    threshold = 90
    url_final = url_api + url_image
    response = requests.get(url_final)
    s = response.text.replace("null", "None")
    temp_dict = eval(s)
    final_dict = temp_dict["tags"]["auto"]
    for key in final_dict:
        if key in key_words:
            if final_dict[key] < threshold:
                print(f"{key} in key words, to low value")
                assert False
        else:
            if final_dict[key] >= threshold:
                print(f"{key} not in key words, high value")
                assert False
    assert True



