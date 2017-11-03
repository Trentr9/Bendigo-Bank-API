from setuptools import setup

setup(name='Bendigo Bank API',
      version='0.1',
      description='A wrapper to access Bendigo Bank account information through the website',
      url='',
      author='Trent Ross',
      author_email='trentross9@gmail.com',
      license='MIT',
      packages=['BendigoBankAPI'],
      install_requires = [
            'requests',
      ],
      zip_safe=False)