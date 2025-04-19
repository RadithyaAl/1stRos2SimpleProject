from setuptools import find_packages, setup

package_name = 'simple_math_loop'

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
    maintainer='deethz',
    maintainer_email='alhamdikaradit@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'math_input_phase = simple_math_loop.input_phase:main',
            'math_first_phase = simple_math_loop.first_phase:main'
        ],
    },
)
