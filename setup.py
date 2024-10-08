from setuptools import setup, find_packages

setup(
    name='protocol_nav_plugin',
    version='0.1',
    py_modules=['protocol_nav_plugin'],
    install_requires=['mkdocs>=1.0'],
    entry_points={
        'mkdocs.plugins': [
            'protocol_nav_plugin = protocol_nav_plugin:ProtocolNavPlugin',
        ]
    }
)