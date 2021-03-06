'''
Created on Mar 9, 2014

@author: Anduril
'''
from setuptools import setup

setup(
        name = "ChorusCore",
        version = "0.9.014",
        description = "A test framework based on unittest, support baselines assertion, give pretty html report",
        author = "Anduril, mxu",
        author_email = "yjckralunr@gmail.com",
        packages = ['ChorusCore'],
        zip_safe = False,
        include_package_data = True,
        install_requires = [
                                'httplib2>=0.8',
                                'Jinja2>=2.6',
                                'mysql-connector-python>=1.0.10',
                                'PIL>=1.1.7',
                                'python-Levenshtein>=0.10.2'
                            ],
        #scripts = ["scripts/chorusrun.py"],
        entry_points = {"console_scripts":['chorusrun=ChorusCore.RunTest:main','chorussetup=ChorusCore.CreateSamples:main']},
        url = "https://github.com/ChorusCore/"
      )
