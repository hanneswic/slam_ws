from setuptools import find_packages, setup

package_name = 'mjpeg_decoder'

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
    maintainer='moonbotslam',
    maintainer_email='hannes-wichert@gmx.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mjpeg_decoder_node = mjpeg_decoder.mjpeg_decoder_node:main',
        ],
    },
)
