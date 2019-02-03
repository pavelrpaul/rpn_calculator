default: help

title:
	@echo "\nRPN Calculator\n"

help: title
	@echo "Usage: make {command}"
	@echo "    run            	run with example.txt file;"
	@echo "    test             test application locally;"
	@echo

run:
	@python3 main.py example.txt

test:
	@pytest
