from setuptools import setup


setup(name='pygments-jscon',
      version='0.1',
      description='A Pygments lexer for JavaScript console',
      author='papaeye',
      author_email='papaeye@gmail.com',
      py_modules=['pygments_jscon'],
      platforms='any',
      license='BSD License',
      entry_points={
        'pygments.lexers': [
            'jsconlexer = pygments_jscon:JavaScriptConsoleLexer'
            ]
        }
      )
