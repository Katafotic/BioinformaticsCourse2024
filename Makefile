all: add_task

last_line="| $(id) | $(title) | :x: | :x: |\n"

start_define_data=$$(grep -n "define DATA" DNA/makefile | head -n 1 | cut -d ":" -f 1)
end_define_data=$$(grep -n "endef" DNA/makefile | head -n 1 | cut -d ":" -f 1)

add_task:
	@echo "\n\nCreate task $(id)"
	
	@mkdir $(id)
	@head -n "$(start_define_data)" DNA/makefile > $(id)/makefile

	@echo "$$data" >> $(id)/makefile
    
	@tail -n +$(end_define_data) DNA/makefile >> $(id)/makefile
	
	@sed -i 's/DNA\./$(id)./g' $(id)/makefile
	
	echo $(last_line) >> README.md


count_python:
	@record_position=$$(grep -n $(id) README.md | tail -n 1 | cut -d ":" -f 1)
	@sed -i '$(record_position) s/:x: | :x:/:white_check_mark: | :x:/g' README.md
	@sed -i '$(record_position) s/:x: | :white_check_mark:/:white_check_mark: | :white_check_mark:/1' README.md
	@echo "Add python solution for $(id)"
	@grep -n $(id) README.md | tail -n 1 | cut -d ":" -f 2-

count_r:
	@record_position=$$(grep -n $(id) README.md | tail -n 1 | cut -d ":" -f 1)
	@sed -i '$(record_position) s/:x: | :x:/:x: | :white_check_mark:/1' README.md
	@sed -i '$(record_position) s/:white_check_mark: | :x:/:white_check_mark: | :white_check_mark:/1' README.md
	@echo "Add R solution for $(id)"
	@grep -n $(id) README.md | tail -n 1 | cut -d ":" -f 2-


count_both:
	@record_position=$$(grep -n $(id) README.md | tail -n 1 | cut -d ":" -f 1)
	@sed -i '$(record_position) s/:x:/:white_check_mark:/g' README.md
	@echo "Task $(id) was solved"
	@grep -n $(id) README.md | tail -n 1 | cut -d ":" -f 2-

reset_status:
	@record_position=$$(grep -n $(id) README.md | tail -n 1 | cut -d ":" -f 1)
	@sed -i '$(record_position) s/:white_check_mark:/:x:/g' README.md
	@echo "Прогресс по задаче $(id) был обнулен"
	@grep -n $(id) README.md | tail -n 1 | cut -d ":" -f 2-

get_status:
	@grep -n "^| $(id) |" README.md | tail -n 1 | cut -d ":" -f 2-

get_statistics:
	@tail -n +$$(grep -n "^| Problem id |" README.md | tail -n 1 | cut -d ":" -f 1) README.md