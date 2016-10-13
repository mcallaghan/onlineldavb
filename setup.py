from setuptools import setup

setup(name='onlineldavb',
      version='0.1',
      description='ONLINE VARIATIONAL BAYES FOR LATENT DIRICHLET ALLOCATION',
      url='https://github.com/mcallaghan/onlineldavb',
      author='Matthew D. Hoffman',
      author_email='mdhoffma@cs.princeton.edu',
      license='MIT',
      packages=['onlineldavb'],
      install_requires=[
          'numpy',
			 'scipy'
      ],
      include_package_data=True,
      zip_safe=False)
