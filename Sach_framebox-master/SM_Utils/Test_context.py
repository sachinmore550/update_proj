""" All variables initializtion and desired capability configuration will be handled in this file"""
import os

class test_context:
    browser = os.environ['Browser']
    test_url = os.environ['test_url']
    implicit_wait = os.environ['implicit_wait']
    platform = os.environ['platform']


