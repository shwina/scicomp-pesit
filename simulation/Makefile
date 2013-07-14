paper.pdf : paper.tex heat.py post_process.py
	python heat.py
	python post_process.py
	pdflatex paper.tex
	rm *.png
	rm *.log
	rm *.aux
	rm *.txt