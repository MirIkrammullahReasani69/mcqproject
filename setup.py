from setuptools import find_packages,setup

setup(
    name = 'MCQPROJECT',
    version = '0.0.1',
    author= 'Mir Ikramullah Reasani',
    author_email= 'ikrammir69@gmail.com',
    install_requires = ["huggingface_hub","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)