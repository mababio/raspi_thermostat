from setuptools import setup, find_packages


version = '.1'

install_requires = ['flask', 'schedule', 'pyyaml', 'singleton-decorator','redis']


setup(name='thermo',
      version=version,
      description="thermo web app",
      classifiers=[],
      keywords='',
      author='Michael Ababio',
      author_email='michaelkwasi@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      zip_safe=False,
      install_requires=install_requires,
      entry_points={
          'console_scripts':
              ['thermo=thermo.temp:main']
      }
      )
