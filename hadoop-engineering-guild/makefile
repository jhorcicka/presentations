# makefile pro LaTeX 

TEX=pdflatex
NAME=main
PDF=hadoop
PACK=$(PDF).zip
SRC=makefile *.tex ./img
VIEWER=evince
BACKUP_DIRECTORY=/home/kuba/docs/code/latex/hadoop
BACKUP_DIRECTORY2=/network/usrshare/kuba/hadoop-guild

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

backup: pack
	cp $(PACK) $(BACKUP_DIRECTORY)
	cp $(PACK) $(BACKUP_DIRECTORY2)

pull: 
	git pull origin master

add: 
	git add ./

commit: 
	git commit 

push: clean add commit
	git push origin master

