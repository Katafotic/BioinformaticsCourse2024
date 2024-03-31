all: test_python

DATA = AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

test_python:
	@echo "Test data is:\t$(DATA)\n\n" 
	@echo "$(DATA)" | python3 DNA.py

test_R:
	@echo "Test data is:\t$(DATA)\n\n" 
	@echo "$(DATA)" | R -f DNA.R --slave


own_input_python:
	@echo "$(INPUT_DATA)" | python3 DNA.py
	
own_input_R:
	@echo "$(INPUT_DATA)" | R -f DNA.R --slave