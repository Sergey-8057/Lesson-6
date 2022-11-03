from setuptools import setup

setup(name='clean_folder',
      version='1',
      description='File sorting',
      url='http://github.com/Sergey-8057/Lesson-6',
      author='Sergey',
      author_email='clean_folder@example.com',
      license='MIT',
      packages=['clean_folder']
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean']}
