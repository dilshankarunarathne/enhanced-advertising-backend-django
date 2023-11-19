from enhanced_advertising_backend_django.mongo import fetch_img_url


def get_ad_img_data(recommended_interest):
    """
    :param recommended_interest: string
    :return: advertisement image
    """

    path = "ad_engine/raw_ads/" + recommended_interest + ".jpg"

    with open(path, "rb") as f:
        return f.read()


def get_ad_img_url(recommended_interest):
    """
    :param recommended_interest: string
    :return: advertisement image url
    """

    # return "https://unstripped-diagonal.000webhostapp.com/banners/" + recommended_interest + ".jpg"

    return fetch_img_url(recommended_interest)
