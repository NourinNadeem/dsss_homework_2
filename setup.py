from setuptools import setup, find_packages

setup(
    name="math_quiz",  # Name of your package
    version="0.1",  # Version number
    packages=find_packages(),  # This will include the math_quiz package
    install_requires=[],  # List of dependencies, if any
    test_suite="math_quiz.tests_math_quiz",  # Point to the tests folder inside math_quiz
    author="Your Name",  # Your name
    author_email="your.email@example.com",  # Your email address
    description="A simple math quiz game",  # Description of the project
    long_description=open("README.md").read(),  # Read from README file
    long_description_content_type="text/markdown",  # Format of the README
    url="https://github.com/yourusername/dsss_homework_2",  # GitHub link
    classifiers=[  # Classifiers for the package (optional but recommended)
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
