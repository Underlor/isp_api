import setuptools

setuptools.setup(
    name='isp_sdk',
    version='0.4.4',
    author="Popov Aleksander",
    author_email="admin@alexue4.ru",
    url="https://github.com/Underlor/isp_api",
    description="ISP Panel Api SDK",
    install_requires=['requests', ],
    packages=setuptools.find_packages(),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
)
