
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

autocomplete:
	@python autocomplete.py

tabs:
	@python tabs.py

toolbox:
	@python toolbox.py

all:
	@make hello1
	@make hello2
	@make grid_layout
	@make form_layout
	@make horizontal_layout
	@make vertical_layout
	@make dialog
	@make calculator
	@make autocomplete
	@make tabs
	@make toolbox


