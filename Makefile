
conda:
	@conda create -n pygt5-env python=3.9

install:
	@pip install -r requirements/conda.txt
