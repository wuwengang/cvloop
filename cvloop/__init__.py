"""Provides cvloop, a ready to use OpenCV VideoCapture mapper, designed for jupyter notebooks."""
import sys

OPENCV_FOUND = False
OPENCV_VERSION_COMPATIBLE = False

try:
    import cv2
    OPENCV_FOUND = True
except ModuleNotFoundError:
    print('OpenCV is not found (tried importing cv2).', file=sys.stderr)
    print('''
    Is OpenCV installed and properly added to your path?
    you are using a virtual environment, make sure to add the path
    to the OpenCV bindings to the environment\'s site-packages.
    For example (MacOSX with brew):
    echo /usr/local/opt/opencv3/lib/python3.6/site-packages > ${HOME}/.virtualenvs/cvloop/lib/python3.6/site-packages/opencv3.pth
    Make sure that the first path contains your cv2.so! (You might have to link it properly.)
    See https://docs.python.org/3/library/site.html
    ''')


if OPENCV_FOUND:
    MAJOR, MINOR, PATCH = cv2.__version__.split('.')
    OPENCV_VERSION_COMPATIBLE = int(MAJOR) >= 3 and int(MINOR) >= 1
    if not OPENCV_VERSION_COMPATIBLE:
        print('OpenCV version {} is lower than 3.1!'.format(cv2.__version__), file=sys.stderr)


if OPENCV_FOUND and OPENCV_VERSION_COMPATIBLE:
    from .cvloop import cvloop
    from .functions import *

