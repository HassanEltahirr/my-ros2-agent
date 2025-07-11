from setuptools import find_packages, setup

package_name = 'crew_agent'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hassaneltahir',
    maintainer_email='100064866@ku.ac.ae',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'crew_agent_node = crew_agent.crew_agent_node:main',
        'manager_node = crew_agent.manager_node:main',
    ],
},

)
