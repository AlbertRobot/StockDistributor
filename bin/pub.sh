#!/usr/bin/env bash

pythonHome=/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
basePath=$(cd `dirname $0`; pwd)

cd ${basePath}

${pythonHome} ../publisher.py