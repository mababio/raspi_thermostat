from setuptools import setup, find_packages


version = '.1'

install_requires = ['flask', 'schedule']


setup(name='thermo',
      version=version,
      description="thermo web app",
      classifiers=[],
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
