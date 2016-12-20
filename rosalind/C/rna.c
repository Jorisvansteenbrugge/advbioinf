#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char * getRNA(char *dna, int dnalen){
    char *rna = malloc((dnalen) * sizeof(char));

    for(int i = 0; i < dnalen; i++){
        switch(dna[i]){
            case 'T':
            case 't':
                rna[i] = 'U';
                break;

            default:
                rna[i] = dna[i];
                break;
        }
    }

    return rna;
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
        char *rna = getRNA(line, strlen(line));
        printf("%s", rna);
    }

}
