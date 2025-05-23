from setuptools import setup, find_packages

setup(
    name='hello-world-project',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    author='Your Name',
    author_email='your@email.com',
    description='A short description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/YourGitHubUsername/Hello-world',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
