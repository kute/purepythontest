#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: simple.py
@ __mtime__: 2016/9/29 13:18


    bg_BG - Bulgarian
    cs_CZ - Czech
    de_DE - German
    dk_DK - Danish
    el_GR - Greek
    en_AU - English (Australia)
    en_CA - English (Canada)
    en_GB - English (Great Britain)
    en_US - English (United States)
    es_ES - Spanish (Spain)
    es_MX - Spanish (Mexico)
    fa_IR - Persian (Iran)
    fi_FI - Finnish
    fr_FR - French
    hi_IN - Hindi
    hr_HR - Croatian
    it_IT - Italian
    ja_JP - Japanese
    ko_KR - Korean
    lt_LT - Lithuanian
    lv_LV - Latvian
    ne_NP - Nepali
    nl_NL - Dutch (Netherlands)
    no_NO - Norwegian
    pl_PL - Polish
    pt_BR - Portuguese (Brazil)
    pt_PT - Portuguese (Portugal)
    ru_RU - Russian
    sl_SI - Slovene
    sv_SE - Swedish
    tr_TR - Turkish
    zh_CN - Chinese (China)
    zh_TW - Chinese (Taiwan)


"""

import random
from faker import Factory
from faker.providers import BaseProvider


class MyProvider(BaseProvider):
    """自定义 属性"""
    def newpropertie(self):
        return random.randint(0, 1000)

# ['_Generator__config', '_Generator__format_token', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__'
# , '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '
# __module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__st
# r__', '__subclasshook__', '__weakref__', 'add_provider', 'address', 'am_pm', 'binary', 'boolean', 'bothify', 'b
# uilding_number', 'century', 'chrome', 'city', 'city_name', 'city_suffix', 'color_name', 'company', 'company_ema
# il', 'company_prefix', 'company_suffix', 'country', 'country_code', 'credit_card_expire', 'credit_card_full', '
# credit_card_number', 'credit_card_provider', 'credit_card_security_code', 'currency_code', 'date', 'date_time',
#  'date_time_ad', 'date_time_between', 'date_time_between_dates', 'date_time_this_century', 'date_time_this_deca
# de', 'date_time_this_month', 'date_time_this_year', 'day_of_month', 'day_of_week', 'domain_name', 'domain_word'
# , 'ean', 'ean13', 'ean8', 'email', 'file_extension', 'file_name', 'firefox', 'first_name', 'first_name_female',
#  'first_name_male', 'first_romanized_name', 'format', 'free_email', 'free_email_domain', 'geo_coordinate', 'get
# _formatter', 'get_providers', 'hex_color', 'image_url', 'internet_explorer', 'ipv4', 'ipv6', 'iso8601', 'job',
# 'language_code', 'last_name', 'last_name_female', 'last_name_male', 'last_romanized_name', 'latitude', 'lexify'
# , 'linux_platform_token', 'linux_processor', 'locale', 'longitude', 'mac_address', 'mac_platform_token', 'mac_p
# rocessor', 'md5', 'mime_type', 'month', 'month_name', 'name', 'name_female', 'name_male', 'null_boolean', 'nume
# rify', 'opera', 'paragraph', 'paragraphs', 'parse', 'password', 'phone_number', 'phonenumber_prefix', 'postcode
# ', 'prefix', 'prefix_female', 'prefix_male', 'profile', 'provider', 'providers', 'pybool', 'pydecimal', 'pydict
# ', 'pyfloat', 'pyint', 'pyiterable', 'pylist', 'pyset', 'pystr', 'pystruct', 'pytuple', 'random', 'random_digit
# ', 'random_digit_not_null', 'random_digit_not_null_or_empty', 'random_digit_or_empty', 'random_element', 'rando
# m_int', 'random_letter', 'random_number', 'random_sample', 'random_sample_unique', 'randomize_nb_elements', 'rg
# b_color', 'rgb_color_list', 'rgb_css_color', 'romanized_name', 'safari', 'safe_color_name', 'safe_email', 'safe
# _hex_color', 'seed', 'sentence', 'sentences', 'set_formatter', 'sha1', 'sha256', 'simple_profile', 'slug', 'ssn
# ', 'state', 'street_address', 'street_name', 'street_suffix', 'suffix', 'suffix_female', 'suffix_male', 'text',
#  'time', 'time_delta', 'timezone', 'tld', 'unix_time', 'uri', 'uri_extension', 'uri_page', 'uri_path', 'url', '
# user_agent', 'user_name', 'uuid4', 'windows_platform_token', 'word', 'words', 'year']


def main():
    fake = Factory.create('zh_CN')
    print(fake.name())
    print(fake.boolean())
    print(fake.bothify())
    print(fake.century())
    print(fake.chrome())
    print(fake.city())
    print(fake.city_name())
    print(fake.city_suffix())
    print(fake.color_name())
    print(fake.company())

    fake.add_provider(MyProvider)
    print(fake.newpropertie())


if __name__ == "__main__":
    main()
