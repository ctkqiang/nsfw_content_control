clean:
	clear
	echo "Cleaning...."
	clear
	rm -r assets/nsfw/__pycache__
	echo "Cleaned"

install:
	clear
	echo "Installing Dependencies...."
	pip3 install opencv-python
	pip3 install nudepy
	pip3 install numpy
	pip3 install --user -U nltk

run:
	clear
	echo "Building Project..."
	clear
	echo "Executing Script..."
	python3 nsfw--opencv.py

info:
	echo "Coded By John Melody"