from distutils.core import setup

setup(
    name = 'PytrackX',
    packages = ['PytrackX'],
    version = '0.1',  # Ideally should be same as your GitHub release tag varsion
    description = 'A general python framework for visual object tracking.',
    author = 'Sriram Kannan, Swetha Saseendran',
    author_email = 'swethasaseendran4@gmail.com',
    url = 'https://github.com/swetha4444/PyTrackX',
    license='MIT',
    packages=['module'],
    install_requires=['numpy>=1.11',
                        'matplotlib>=1.5'],
    keywords = ['yolo', 'mediapipe','object detection','object tracking'],
    classifiers = [],
)