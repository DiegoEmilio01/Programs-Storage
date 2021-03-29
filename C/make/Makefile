main: main.o dog.o
	gcc main.o dog.o -o main

main.o: main.c dog.h
	gcc main.c -c -o main.o

dog.o: dog.c dog.h
	gcc dog.c -c -o dog.o