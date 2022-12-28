from setuptools import setup, find_packages
import locking

from os import path


with open('requirements/requirements.txt') as f:
    install_requires = [ r for r in f.read().splitlines() if not r.strip().startswith("#") ]

with open('requirements/requirements.txt') as f:
    tests_require = [ r for r in f.read().splitlines() if not r.strip().startswith("#") ]

setup(
    name="django-db-locking",
    version=locking.__version__,
    url='https://github.com/vikingco/django-db-locking/',
    license='BSD',
    description='Database locking',
    long_description=open('README.rst', 'r').read(),
    author='VikingCo',
    author_email='operations@unleashed.be',
    packages=find_packages('.'),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={'celery':  ["celery"] },
    tests_require=tests_require,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
