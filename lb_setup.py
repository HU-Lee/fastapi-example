from setuptools import setup
setup(
    name='loadbalance',
    version='0.0.1',
    packages=[
        'loadbalance',
        'loadbalance.balance',
    ],
    install_requires=[
        'requests',      # 최신버전 설치
        "pywin32 >= 1.0;platform_system=='Windows'", # 플랫폼 구분
        'python_version >= "3.5"',
    ],
)

# python lb_setup.py bdist_wheel