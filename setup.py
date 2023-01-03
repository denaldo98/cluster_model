import setuptools

setuptools.setup(
    name='cluster_model',
    version='0.0.1',
    author='Denaldo Lapi',
    author_email='denaldo98@gmail.com',
    description='Class for wrapping River cluster model for BERTopic Online Topic Modeling',
    long_description='',
    long_description_content_type="text/markdown",
    url='https://github.com/denaldo98/cluster_model',
    license='MIT',
    packages=['cluster_model'],
    install_requires=['river'],
)