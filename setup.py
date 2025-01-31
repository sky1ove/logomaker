from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='logomaker-kinase',
      version='0.8.3',
      description='Modified Logomaker package for making kinase substrate motif',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
      ],
      keywords='Sequence Logos',
      url='http://logomaker.readthedocs.io',
      author='Lily',
      author_email='lcai888666@gmail.com',
      license='MIT',
      packages=['logomaker'],
      include_package_data=True,
      install_requires=[
        'numpy',
		    'matplotlib',
		    'pandas'
      ],
      zip_safe=False)