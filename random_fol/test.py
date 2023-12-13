# def sum(a,b):
#     return a+b
#
# sum = sum(5,6)
# print(sum)
#
# class Mathops:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         return self.a+self.b
#
# obj = Mathops(4,5)
# sum= obj.sum()
# print(sum)

#novemberautomation2023
#novemberautomationbatch@gmail.com

"""
# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

name: Python application

on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]

permissions:
  contents: read

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Execute python file
      run: python main.py
    - name: Execute another python file
      run: python test/Hello_world.py
"""


