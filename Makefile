all: add_task

last_line="| $(id) | $(title) | :x: | :x: |\n"

add_task:
	mkdir $(id) 
	sed 's/DNA/$(id)/g' DNA/makefile > $(id)/makefile
	echo $(last_line) >> README.md

