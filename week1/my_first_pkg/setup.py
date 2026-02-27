from setuptools import find_packages, setup

package_name = 'my_first_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Hassan Maqsood',
    maintainer_email='2022-MC-18@student.uet.edu.pk',
    description='Week 1 ROS 2 package - MCT-454L',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_node = my_first_pkg.simple_node:main',
            'counter_node = my_first_pkg.counter_node:main',
            'param_node = my_first_pkg.param_node:main',
        ],
    },
)
