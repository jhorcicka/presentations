# makefile pro LaTeX 

TEX=pdflatex
NAME=main
PDF=productivity
PACK=productivity.zip
SRC=makefile *.tex ./img
VIEWER=evince
BACKUP_DIR=/netapp/usrshare/jakubh/engineering-guilds/2020-09-work-productivity

all: compile rename run

backup: pack
	cp $(PACK) $(BACKUP_DIR)

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

