import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gutenberg-py",
    author="Peter Rauscher",
    author_email="peterrauscher@protonmail.com",
    description="A library to access the Project Gutenberg API",
    keywords="gutenberg, project-gutenberg, ebooks, books",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/peterrauscher/gutenberg-py",
    project_urls={
        "Documentation": "https://github.com/peterrauscher/gutenberg-py",
        "Bug Reports": "https://github.com/peterrauscher/gutenberg-py/issues",
        "Source Code": "https://github.com/peterrauscher/gutenberg-py",
        "Funding": "https://ko-fi.com/peterrauscher",
        # 'Say Thanks!': '',
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        # see https://pypi.org/classifiers/
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    python_requires=">=3.7",
    install_requires=["requests"],
    extras_require={
        "dev": ["check-manifest"],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=gutenberg:main',
    # You can execute `run` in bash to run `main()` in src/gutenberg/__init__.py
    #     ],
    # },
)
