from setuptools import setup


setup(
    name='keylogger',
    version='1.0',
    install_requires=[
        'pynput==1.7.6',
        'requests==2.25.1'
    ],
    scripts=['keylogger.py'],
)