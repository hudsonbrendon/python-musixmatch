from setuptools import setup


setup(name='pymusixmatch',
      version='0.2',
      description='Simple integrate of API musixmatch.com with python',
      url='https://github.com/hudsonbrendon/python-musixmatch',
      author='Hudson Brendon',
      author_email='contato.hudsonbrendon@gmail.com',
      license='MIT',
      packages=['musixmatch'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
