"""

    Declare a Python package aansite.theme

"""

from setuptools import setup, find_packages

setup(name = "aansite.theme",
    version = "1.0",
    description = "A Plone theme product",
    author = "Kamon Ayeva",
    author_email = "kamon.ayeva@gmail.com",
    url = "",
    packages = find_packages(exclude=['ez_setup']),
    namespace_packages = ['aansite'],
    include_package_data = True,
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],     
    license="GPL2",
    install_requires = [
        "setuptools",
        "five.grok", 
        "z3c.jbot", 
    ],
    entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,        
) 
