#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import os
import re

if __name__ == '__main__':
    d = re.findall("d\d+", os.getcwd())[0][1:]
    x = requests.get(f'https://adventofcode.com/2024/day/{d}')
    prob = ""
    if x.status_code == 200:
        soup = BeautifulSoup(x.content, 'lxml')
        for x in soup.find_all('code'):
            prob = max(prob, x.text, key=len)
        with open('sample', 'w') as f:
            f.write(prob)
        x = requests.get(f'https://adventofcode.com/2024/day/{d}/input', cookies={
            'session': '53616c7465645f5f846dee2063c3b723077df4250701fc21c16d6c148587d09ca61433e4d5c494d94738fe65ec168b8d01cccf35d17b08447c09c0545f5d6112',
        })
        with open('input', 'wb') as f:
            f.write(x.content)
    else:
        print("Error: ", x.status_code)