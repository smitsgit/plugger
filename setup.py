from setuptools import setup

setup(
    name='plugg',
    version='1',
    description='A plugin demo',
    author='Smital Desai',
    author_email='coolsmital@coolio.io',
    packages=['plugger', 'formatters'],
    entry_points={
        'pytimed': [
            'json = formatters.json_formatter:get_format',
            'yaml = formatters.yaml_formatter:get_format'
        ]
    }
)
