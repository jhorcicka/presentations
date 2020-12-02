
MAIN=main.py
ARGS=""
SRC=*.py 
PACK=mainPython.zip

all: clear run

run: $(MAIN)
	./$(MAIN) $(ARGS)

clear: 
	clear

permission: 
	chmod +x $(MAIN)

pack: 
	zip -r $(PACK) $(SRC) makefile

edit:
	gvim -p *.py
