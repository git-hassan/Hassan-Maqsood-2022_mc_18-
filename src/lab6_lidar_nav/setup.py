from setuptools import setup

package_name = 'lab6_lidar_nav'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Hassan Maqsood',
    maintainer_email='hassan@example.com',
    description='Lab 6 - LiDAR Reactive Navigation',
    license='MIT',
    entry_points={
        'console_scripts': [
            'lidar_navigator = lab6_lidar_nav.lidar_navigator:main',
        ],
    },
)
