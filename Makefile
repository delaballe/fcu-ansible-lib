.PHONY: build install clean

build:
	python setup.py build;

install:
	python setup.py install;
	make clean;

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf build dist src/*.egg-info;

default: build
