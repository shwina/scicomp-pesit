paper.pdf : heat.py post_process.py paper.tex
	python heat.py
	python post_process.py
	pdflatex paper.tex
	rm *.png
	rm *.log
	rm *.aux
	rm *.txt