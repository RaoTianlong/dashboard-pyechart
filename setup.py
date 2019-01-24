import setuptools

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="dashboard-pyechart",
    version="0.0.1",
    author="Jason Rao",
    author_email="raotl1995@gmail.com",
    description="A easy dashboard package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="没有",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Common Public License",
        "Operating System :: Microsoft",
    ],
)