import os

from setuptools import find_packages, setup

project_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(project_dir, "version.txt")) as f:
    version = f.read().rstrip()

# We use the .in file because a library shouldn't pin versions, it breaks consumers'
# updates. We allow commented lines in this file
with open(os.path.join(project_dir, "requirements", "base.in")) as f:
    requirements_raw = f.readlines()

requirements_without_comments = [
    line for line in requirements_raw if line and not line.startswith("#")
]

setup(
    name="mozilla-repo-urls",
    version=version,
    description="Process Mozilla's repository URLs. "
    "The intent is to centralize URLs parsing.",
    author="Mozilla Release Engineering",
    author_email="release+python@mozilla.com",
    url="https://github.com/mozilla-releng/mozilla-repo-urls",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license="MPL2",
    install_requires=requirements_without_comments,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
