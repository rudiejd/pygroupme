import setuptools

# pygroupme 1.0 by JD Rudie
# TODO: add group information, more functions

with open("README.MD", 'r') as ld:
    long_desc = ld.read()

setuptools.setup(name='pygroupme',
                 version='0.0.2',
                 description='Easy use of the GroupMe API with Python',
                 long_description=long_desc,
                 author='JD Rudie',
                 author_email='rudiejd@miamioh.edu',
                 long_description_content_type='text/markdown',
                 packages=setuptools.find_packages(),
                 install_requires=['requests'],
                 classifiers=[
                    'Programming Language :: Python :: 3',
                    'License :: OSI Approved :: MIT License',
                    'Operating System :: OS Independent',
                 ]
                 )
