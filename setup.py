import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="quart-admin",
    version="2.0.3",
    description="A tool to create quart projects faster with a scalable setup",  # Optional
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shahriyardx/quart-admin",
    author="Md Shahriyar Alam",
    author_email="contact@shahriyar.dev",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={"console_scripts": ["quart-admin = quart_admin:cli"]},
    keywords="quart, quart-admin",
    packages=find_packages(),
    python_requires=">=3.7, <4",
    install_requires=["quart", "click", "python-slugify"],
    project_urls={
        "Bug Reports": "https://github.com/shahriyardx/quart-admin/issues",
        "Source": "https://github.com/shahriyardx/quart-admin/",
    },
)
