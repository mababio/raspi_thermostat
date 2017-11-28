from setuptools import setup, find_packages
import sys, os



version = '.1'

install_requires = [
	'flask'

]


setup(name='thermo',
    version=version,
    description="thermo web app",
    #long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='',
    author='Michael Ababio',
    author_email='michaelkwasi@gmail.com',
    url='',
    license='',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['thermo=thermo.temp:main']
    }
)
