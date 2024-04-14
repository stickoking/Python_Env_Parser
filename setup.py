from setuptools import setup, find_packages

setup(
    name="py_env_parser",
    version="0.1",
    author="Prasshant Shanmugalingam",  # Replace with your name
    description="A Simple env file parser",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/my_package",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)