import sys
from setuptools import setup

install_requires = [
    'jsonschema>=2.4.0',
    'click>=6.6'
]

setup(
    name='socdat',
    version='0.0.1',
    description='A tool for dealing with Socrata',
    long_description=open('README').read(),
    author='Dan Nguyen',
    author_email='dan@danwin.com',
    url='http://danwin.com',
    license='MIT',
    classifiers=[
        'Development Status :: 0 - WTF',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: Data Wrangling',
        'Topic :: Open Data'
    ],
    packages=[
        'socdat',
    ],
    entry_points ={
        'console_scripts': [
            'socdat-info = socdat.utilities.info:launch_new_instance',
        ]
    },
    install_requires = install_requires
)
