from setuptools import setup
from setuptools import find_packages
 
 
setup(
    name='optimizely-platform',
    version='0.0.5',
    description='Package providing modules needed to build add-ons that run natively in the Optimizely platform.',
    author='Jon Gaulding, Tyler Jones, Peng-Wen Chen, Ali Rizvi',
    author_email='jon@optimizely.com',
    url='https://github.com/optimizely/optimizely_platform',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Environment :: Web Environment',
      'Intended Audience :: Developers',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(
      exclude=['tests']
    )
)
