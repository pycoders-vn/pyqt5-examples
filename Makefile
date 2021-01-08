
conda:
	@conda create -n pygt5-env python=3.9

install:
	@pip install -r requirements/conda.txt


# Run example PyQt5 application
hello1:
	@python hello_gui.py

hello2:
	@python hello_pyqt5.py

grid_layout:
	@python grid_layout.py

form_layout:
	@python form_layout.py

horizontal_layout:
	@python horizontal_layout.py

vertical_layout:
	@python vertical_layout.py

dialog:
	@python dialog.py

calculator:
	@python calculator.py


