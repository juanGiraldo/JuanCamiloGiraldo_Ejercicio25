sample.pdf: ./sample 10000 0 0.4
	python sample.py

sample: sample.c
	gcc -o sample sample.c -lm

clean :
	rm -rf sample.pdf sample sample.dat
