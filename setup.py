from setuptools import setup, find_packages

setup(
    name='BinaryOptionstools',
    version='0.1.0',
    author='Vigo',
    author_email='vigopaul05@gmail.com',
    description='Tools for Binary Options trading',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/BinaryOptionstools',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List your dependencies here, e.g.
        'numpy',
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
