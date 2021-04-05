.PHONY: env

env: env/Scripts/activate

env/Scripts/activate:
	python -m virtualenv -p python3 env
	pip install --upgrade pip

install-local:
	# update remote packages to local installation
	pip install --editable .

install-remote:
	# update local packages to remote address
	pip install . -t ${TOOLS_INST_PATH}/dcc-tools

clean-env:
	rm -fr dcc-tools-env

clean: 
	rm -fr ${TOOLS_INST_PATH}/dcc-tools