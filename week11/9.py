# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Zf9FALuFGoo31qbOvUDqhRIEi_petyq
"""

living_cost_dict = {
    '臺北市': 17005,
    '新北市': 15500,
    '桃園市': 15281,
    '臺中市': 14596,
    '臺南市': 12388,
    '高雄市': 13099,
    '非六都之縣市': 12388,
    '金門縣連江縣': 11648
}
living_area = input("請輸入您的居住縣市:")
try:
    living_cost = living_cost_dict[living_area]
    print("{}的每人每月最低生活費為{:,}".format(living_area, living_cost))
except KeyError:
    print("請重新輸入居住縣市")