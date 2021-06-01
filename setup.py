import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="obscurepy",
    version="0.7.0",
    author="Andrew Christiansen",
    author_email="andrewtaylorchristiansen@gmail.com",
    description=" A tool for obscuring, or making python source difficult to read. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drewtchrist/obscurepy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=[
        'Click',
        'astunparse',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'obscure = obscurepy.scripts.obscure:obscure'
        ],
    },
)
