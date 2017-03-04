from setuptools import setup
setup(name='tele-manager',
      version='0.0.1',
      description="""
Tele-Manager is the Telegram Bot solution for group or personal data storage / retrieval sent to him.
""",
      url='https://github.com/0x00-0x00/tele-manager.git',
      author='zc00l',
      author_email='andre.marques@fatecp.sp.gov.br',
      license='MIT',
      packages=['telemanager'],
      package_dir={'telemanager': 'src'},
      package_data={'telemanager': ['src/*']},
      scripts=['bin/telemanager'],
      zip_safe=False)
