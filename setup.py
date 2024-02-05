from setuptools import setup

setup(
    name='DecisionMakerSkill',
    version='0.1',
    description='A Mycroft skill for making decisions',
    author='Your Name',
    author_email='your.email@example.com',
    packages=['skill-dec'],  # Adjust the package name accordingly
    install_requires=[
        'ovos',
    ],
    entry_points={
        'ovos.skill': [
            'DecisionMakerSkill = skill_dec:DecisionMakerSkill'
        ],
    },
)
