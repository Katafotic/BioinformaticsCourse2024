all: add_task

last_column="| $(id) | $(title) | :x: | :x: |\n"

add_task:
	mkdir $(id) 
	cp DNA/makefile $(id)/
	echo $(last_column) >> README.md
