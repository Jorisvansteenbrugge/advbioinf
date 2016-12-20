#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char * getRevc(char *dna, size_t dnalen){
    char *revc = malloc((dnalen) * sizeof(char));
//rev: len -1 -i
    for(int i = 0; i < dnalen; i++){
        switch(dna[i]){
            case 'T':
            case 't':
                revc[i] = 'A';
                break;
            case 'a':
            case 'A':
                revc[i] = 'T';
                break;
            case 'c':
            case 'C':
                revc[i] = 'G';
                break;
            case 'g':
            case 'G':
                revc[i] = 'C';
                break;

        }
    }

    return revc;
}

int main(int argc, char *argv[]){
    FILE *fp;
    char *filepath = argv[1];
    size_t len = 0;
    ssize_t read;
    char *line= NULL;

    fp = fopen(filepath, "r");
    if (fp == NULL){
        exit(1);
    }

    while((read = getline(&line, &len, fp)) != -1){
        char *revc = getRevc(line, strlen(line));
        printf("%s\n", revc);
    }

}
