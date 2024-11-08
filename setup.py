from setuptools import setup

setup(
    name="kalyanram",
    version="0.0.8",
    author="V Kalyan Ram",
    author_email="vrchinnarathod@gmail.com",
    description="A brief description of the kalyanram package.",
    long_description=open("README.rst", "r", encoding="utf-8").read(),
    long_description_content_type="text/x-rst",  # Specify that the long description is in reStructuredText
    url="",  # Add the URL for the project or repository if available
  # Automatically find packages in the directory
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",  # Add a development status
        "Intended Audience :: Developers",  # Specify intended audience
        "Topic :: Software Development :: Libraries",  # Specify topic
    ],
    python_requires='>=3.6',  # Specify the required Python version
    install_requires=[  # List any dependencies your package needs
        # 'dependency_name>=version',  # Uncomment and add your dependencies here
    ],
)
