Interpreter=python
Formatter=autopep8
Linter=pylint

all: format #lint

format:
	${Formatter} *.py --in-place

lint:
	${Linter} *.py
