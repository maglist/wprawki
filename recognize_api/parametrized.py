import pytest
from recognize_api.simple_test import check_picture

@pytest.mark.parametrize('url_image, key_words', [
    ('"https://ichef.bbci.co.uk/news/976/cpsprodpb/12A9B/production/_111434467_gettyimages-1143489763.jpg"', ["cat", "animal", "mammal", "pet"]),
    ("https://kidbluboo.files.wordpress.com/2016/11/office-people-images-people-in-the-office-903884-8-1.jpg", ["human", "apparel", "person", "suit", "accessories", "accessory", "clothing", "coat", "finger", "overcoat", "thumbs up", "tie"])
])
def test_check_images(url_image, key_words):
    check_picture(url_image, key_words)