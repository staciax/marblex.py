from setuptools import setup
import re

requirements = [
    'requests',
]

version = ''
with open('marblex/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

readme = ''
with open('README.md') as f:
    readme = f.read()

setup(
    name='marblex.py',
    author='xStacia',
    url='https://github.com/staciax/marblex.py',
    project_urls={
        "Issue tracker": "https://github.com/staciax/marblex.py/issues",
    },
    version=version,
    packages=['marblex'],
    license='MIT',
    description='A library to get various cryptocurrency prices from the marblex API',
    long_description=readme,
    install_requires=requirements,
    python_requires='>=3.6.0',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
