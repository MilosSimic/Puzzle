from setuptools import setup, find_packages

setup(name='puzzle',
      version='0.1',
      description='Simple plugin framework',
      url='https://github.com/MilosSimic/Puzzle',
      author='Milos Simic',
      author_email='milossimicsimo@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data= True,
      zip_safe=False
)