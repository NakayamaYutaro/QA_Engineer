'''
モジュール名： 「csvdct.py」
最終変更日時：　2020/12/09
説明： 学習用csvデータを自動生成するプログラム
コーディング担当：Yutaro Nakayama

#sales_grouth_rate（売上成長率の計算）
売上高伸び率＝(当年度売上高―前年度売上高)/前年度売上高
'''

import csv
import random
import numpy as np

with open('data/data_set.csv','w') as csv_file:
    #elapsed_years, capital, annual sales, number of employees, sales growth rate(avg in japanese), unlisted, double loan
    fieldnames = ['設立後経過年','資本金','年間売上高','社員数','売上高成長率','非上場性','複融資']
    writer = csv.writer(csv_file)
    writer.writerow(fieldnames)
   
    double_loan = [0,1]#「複融資なし：[0]、複融資あり[1]」
    double_loan_rate = [0.7,0.3]

    for i in range(1,2000):
        year = random.weibullvariate(0.5, 0.1) #単位「年」
        capital = random.weibullvariate(2500, 500)#単位「万」
        annual_sale = random.lognormvariate(1, 0.5)#単位「億」
        sales = random.weibullvariate(20, 10)#単位「人」
        sales_growth_rate = random.weibullvariate(0.6, 0.1)#単位「%」
        unlisted = random.randint(0, 1)#「非上場性：[0]非上場、[1]上場」
        double_loan_res = np.random.choice(a=double_loan, size=1, p=double_loan_rate) 
        data_row = [year, capital, annual_sale, sales, sales_growth_rate, unlisted, double_loan_res]
        writer.writerow(data_row)
csv_file.close()
