from setuptools import setup, find_packages
import os

version = '0.1'

long_description = open(os.path.join(__file__,'../README')).read()


setup(name='gae_taggable_mixin',
      version=version,
      description="A mixin class that adds taggability to Google AppEngine Model classes.",
      long_description=long_description,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: GAE',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        ], 
      author="Anatoly Bubenkov",
      author_email="bubenkoff@gmail.com",
      url="http://bubenkoff.me",
      license="GPL",
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        ],
      )
