%.pdf : %.tex
	for FILE in $^; do pdflatex $$FILE; done
	rm *.aux
	rm *.log

