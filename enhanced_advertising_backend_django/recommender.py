from iengine.ad_recommender_package import recommend_topic


def predict_interest(age_group: str, gender_string: str) -> str:
    """
    :param age_group:   (0-2), (4-6), (8-12), (15-20), (25-32), (38-43), (48-53), (60-100)
    :param gender_string:   Male, Female
    :return: recommended interest
    """
    gender = None
    age = None

    # parse gender
    if gender_string == 'Male':
        gender = 'M'
    elif gender_string == 'Female':
        gender = 'F'
    else:
        raise ValueError

    # parse age
    if age_group == '(0-2)':
        age = 2
    elif age_group == '(4-6)':
        age = 6
    elif age_group == '(8-12)':
        age = 12
    elif age_group == '(15-20)':
        age = 19
    elif age_group == '(25-32)':
        age = 27
    elif age_group == '(38-43)':
        age = 41
    elif age_group == '(48-53)':
        age = 51
    elif age_group == '(60-100)':
        age = 62

    return recommend_topic(age, gender)

