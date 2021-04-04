.PHONY: venv

venv: venv/Scripts/activate

venv/Scripts/activate:
	python -m virtualenv -p python3 venv
	pip install --upgrade pip

install-local:
	# update remote packages to local installation
	pip install --editable .

install-remote:
	# update local packages to remote address
	pip install . -t ${TOOLS_INST_PATH}/dcc-tools

clean-venv:
	rm -fr dcc-tools-venv

clean: 
	rm -fr ${TOOLS_INST_PATH}/dcc-tools