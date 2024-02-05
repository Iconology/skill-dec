from setuptools import setup

setup(
    name='DecisionMakerSkill',
    version='0.1',
    description='A Mycroft skill for making decisions',
    author='Your Name',
    author_email='your.email@example.com',
    packages=['decision_maker_skill'],
    install_requires=[
        'ovos',
    ],
    entry_points={
        'ovos.skill': [
            'DecisionMakerSkill = decision_maker_skill:DecisionMakerSkill'
        ],
    },
)
