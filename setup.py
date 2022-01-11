from distutils.core import setup
import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name = 'PytrackX',
    packages = ['PytrackX'],
    version = '0.1',  # Ideally should be same as your GitHub release tag varsion
    description = 'A general python framework for visual object tracking.',
    long_description= long_description,
    long_description_content_type="text/markdown",
    author = 'Sriram Kannan, Swetha Saseendran',
    author_email = 'swethasaseendran4@gmail.com',
    url = 'https://github.com/swetha4444/PyTrackX',
    license='MIT',
    project_urls={
        "Bug Tracker": "https://github.com/swetha4444/PyTrackX/issues",
    },
    install_requires=['numpy>=1.11',
                        'matplotlib>=1.5',
                        'pandas',
                        'cv2',
                        'scipy',
                        'mediapipe',
                        'time'],
    download_url= 'https://github.com/swetha4444/PyTrackX/archive/refs/tags/0.1.tar.gz',
    keywords = ['yolo', 'mediapipe','object detection','object tracking'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
