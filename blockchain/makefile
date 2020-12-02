# makefile pro LaTeX 

TEX=pdflatex
NAME=main
PDF=blockchain
PACK=$(PDF).zip
SRC=makefile *.tex ./img
VIEWER=okular

all: compile rename run

compile:
	pdflatex $(NAME).tex

rename: $(NAME).pdf
	mv $(NAME).pdf $(PDF).pdf

run: $(PDF).pdf
	$(VIEWER) ./$(PDF).pdf

clean:
	rm -f ./*.aux ./*.dvi ./*.log ./*.zip ./*.bbl ./*.ps ./*.dvi ./*.blg ./*.nav ./*.out ./*.snm ./*.toc

pack: clean $(SRC)
	zip -r $(PACK) $(SRC)

edit:
	gvim -p $(NAME).tex *.bib

