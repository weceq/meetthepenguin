"""setup.py
"""
import os

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(HERE, 'CHANGES.rst')) as f:
    CHANGES = f.read()

REQUIRES = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    ]

TEST_REQUIRES = [
    'nose',
    'coverage',
    'webtest',
    ]

DEV_REQUIRES = [
    'pylint',
    'bumpversion',
    'sphinx',
    ]

setup(name='meetthepenguin',
      version='0.0',
      description='meetthepenguin',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Dawid Grzegorz Węckowski',
      author_email='weceq@tlen.pl',
      url='https://github.com/weceq/meetthepenguin',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='meetthepenguin',
      install_requires=REQUIRES,
      extras_require={
          'test': TEST_REQUIRES,
          'dev': DEV_REQUIRES
      },
      entry_points="""\
      [paste.app_factory]
      main = meetthepenguin:main
      [console_scripts]
      initialize_meetthepenguin_db = meetthepenguin.scripts.initializedb:main
      """,
     )
