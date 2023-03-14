from setuptools import setup, find_packages

setup(
    name="api_project_1",
    version="0.0.1",
    author="copied from Edidiong Etuk",
    author_email="edeediong@gmail.com",
    long_description_content_type = 'text/markdown',
    url="https://bit.ly/edeediong-resume",
    description="timezones",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["timechecker = src.main:main"]},
)
