from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="question_generation",
    packages=find_packages(),
    version="0.0.0",
    url="https://github.com/patil-suraj/question_generation",
    license="MIT",
    author="Suraj Patil",
    author_email="surajp815@gmail.com",
    description="Question generation is the task of automatically generating questions from a text paragraph.",
    install_requires=["transformers==4.18.0", "nltk==3.7", "nlp>=0.2.0", "torch==1.11.0"],
    python_requires=">=3.6",
    include_package_data=True,
    platforms="any",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
