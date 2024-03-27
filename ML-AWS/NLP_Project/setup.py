import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = "NLP_Project"
AUTHOR_USERNAME = "dhruvshah01"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "dhruvsh0111@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    description="Text Summarizer",
    Long_description=long_description,
    Long_description_content_type="text/markdown",
    url="https://github.com/dhruvshah01/ML-AWS/NLP_Project",
    project_urls={
        "Bug Tracker": "https://github.com/dhruvshah01/ML-AWS/NLP_Project/issues"
    },
    package_dir={"" : "src"},
    packages=setuptools.find_packages(where='src')
)
