from enhanced_advertising_backend_django.mongo import get_all_stats, put_stat
from datetime import datetime


def get_month():
    now = datetime.now()
    return now.strftime('%B').lower()


def populate():
    statistics = get_all_stats(get_month())
    print(dict(statistics)['male_4_12'])

    return statistics


def populate_with_month(month):
    statistics = get_all_stats(month)
    print(dict(statistics)['male_4_12'])

    return statistics


def update(age_group, gender):
    print("stat update called for ", age_group, " ", gender)

    stat = populate()

    print(stat)

    if age_group == '(4-6)' or age_group == '(8-12)':
        stat['total_4_12'] = stat['total_4_12'] + 1
        if gender == 'Male':
            stat['male_4_12'] = stat['male_4_12'] + 1
            stat['total_male'] = stat['total_male'] + 1
        elif gender == 'Female':
            stat['female_4_12'] = stat['female_4_12'] + 1
            stat['total_female'] = stat['total_female'] + 1

    elif age_group == '(15-20)':
        stat['total_13_26'] = stat['total_13_26'] + 1
        if gender == 'Male':
            stat['male_13_26'] = stat['male_13_26'] + 1
            stat['total_male'] = stat['total_male'] + 1
        elif gender == 'Female':
            stat['female_13_26'] = stat['female_13_26'] + 1
            stat['total_female'] = stat['total_female'] + 1

    elif age_group == '(25-32)' or age_group == '(38-43)':
        stat['total_27_40'] = stat['total_27_40'] + 1
        if gender == 'Male':
            stat['male_27_40'] = stat['male_27_40'] + 1
            stat['total_male'] = stat['total_male'] + 1
        elif gender == 'Female':
            stat['female_27_40'] = stat['female_27_40'] + 1
            stat['total_female'] = stat['total_female'] + 1

    elif age_group == '(48-53)' or age_group == '(60-100)':
        stat['total_above_40'] = stat['total_above_40'] + 1
        if gender == 'Male':
            stat['male_above_40'] = stat['male_above_40'] + 1
            stat['total_male'] = stat['total_male'] + 1
        elif gender == 'Female':
            stat['female_above_40'] = stat['female_above_40'] + 1
            stat['total_female'] = stat['total_female'] + 1

    put_stat(stat)


# update('(15-20)', 'Female')
# print(populate())
