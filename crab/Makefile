# Makefile for BDT codes

# $< = name of first dependancy
# $@ = name of target ("main")
# -c ask the compiler not to link
# -o specify target
#

#Define variables
CC=g++ #Compiler used
DEBUG = -g
CFLAGS = -c  $(DEBUG) #Compilation options
# LFLAGS = $(DEBUG) -L/home/nico/root/lib -lTMVA -lTMVAGui
LFLAGS = $(DEBUG) -lTMVA #-lTMVAGui
ROOTFLAGS = `root-config --glibs --cflags`

SRCS = $(wildcard *.cc) #Source files are all files with .cc extension
HDRS = $(wildcard *.h) #Header files are all files with .h extension
OBJS = $(SRCS:.cc=.o) #Object files are all files with .o extension, which have same names as source files

CREATE_FILES = Create_JobFiles_AllSteps.exe #Name of executable file

# .PHONY : $(CREATE_FILES)  #Force to always recompile object




#Instructions
all: $(CREATE_FILES)

#Obtain executables from object files
$(CREATE_FILES) : Create_JobFiles_AllSteps.cxx ../Helper_Functions.h
	@echo "-- Creating executable ./$(CREATE_FILES) --"
	@$(CC) Create_JobFiles_AllSteps.cxx -o $@ $(ROOTFLAGS) $(LFLAGS)
	@echo "-- Done --"

#Obtain objects from source and header files
%.o: %.cc
	@echo "-- Compiling --"
	@$(CC) $(ROOTFLAGS) $(CFLAGS) $< -o $@



#Erase all objects and executable
clean:
	@-rm -f *.o *.exe

