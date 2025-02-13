import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description=f.read()

version="0.0.0"

REPO_NAME="Text-Summerizer-Project-"
AUTHOR_NAME ="HarshadaSalle"
SRC_REPO ="textsummerizer"
AUTHOR_EMAIL ="harshadasalle@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=version,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for nlp app",
    Long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",

    project_urls={  # Fixed this
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),


)
