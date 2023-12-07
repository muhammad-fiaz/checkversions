from setuptools import setup, find_packages

from checkversions.version import get_Version

VERSION = "0.0.2"

get_Version(VERSION)

DESCRIPTION = 'CheckVersions is a powerful and intuitive version comparison tool for software development.'

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as req_file:
    INSTALL_REQUIRES = req_file.read().splitlines()

setup(
    name="checkversions",
    version=VERSION,
    author="Muhammad Fiaz",
    author_email="contact@muhammmadfiaz.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/muhammad-fiaz/checkversions.git',
    packages=find_packages(),
    keywords=[
        'version comparison', 'software development', 'semantic versioning',
        'version control', 'software versioning', 'release management'
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.8',
    install_requires=INSTALL_REQUIRES,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    license='MIT License',
    project_urls={
        'Source Code': 'https://github.com/muhammad-fiaz/checkversions.git',
        'Bug Tracker': 'https://github.com/muhammad-fiaz/checkversions/issues',
        'Documentation': 'https://github.com/muhammad-fiaz/checkversions#readme',
    },
)

print("Happy Creative!")
