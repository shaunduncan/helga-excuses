from setuptools import setup, find_packages

setup(
    name='helga-excuses',
    use_hg_version=True,
    author="Alfredo Deza",
    author_email="contact@deza.pe",
    url="https://github.com/alfredodeza/helga-excuses",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'BeautifulSoup',
        'requests',
    ],
    entry_points = dict(
        helga_plugins = [
            'excuses = helga_excuses:excuses',
        ],
    ),
)
