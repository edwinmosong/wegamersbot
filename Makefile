VENV=./python_env

python_env: FORCE
	@if [ -a $(VENV) ]; then\
		echo "Virtualenv $(VENV) exists. Activate it by running '. $(VENV)/bin/activate'" ; \
	else \
		mkdir $(VENV); \
		virtualenv -p python3 $(VENV); \
		. $(VENV)/bin/activate; \
		echo "Installing libs in $(VENV)"; \
		pip3 install -r ./requirements.txt; \
		echo "Done installing libs"; \
	fi
	@. $(VENV)/bin/activate

clean:
	@if [ -a $(VENV) ]; then\
		echo "Cleaning virtualenv $(VENV)"; \
		rm -rf $(VENV); \
	fi

FORCE:
