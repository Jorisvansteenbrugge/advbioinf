#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int * getCounts(char *dna, int dnalen){

    int t = 0;
    int c = 0;
    int a = 0;
    int g = 0;
    int *counts = malloc(5* sizeof(int));
    for(int i=0;i<dnalen;i++)
    {
        char nuc = dna[i];
        switch (nuc)
        {
            case 'a':
            case 'A':
                a++;
                break;
            case 't':
            case 'T':
                t++;
                break;
            case 'c':
            case 'C':
                c++;
                break;
            case 'g':
            case 'G':
                g++;
                break;

        } 
    }
    counts[0] = a;
    counts[1] = c;
    counts[2] = g;
    counts[3] = t;

    return counts;
}


int main(int argc, char *argv[]){
    FILE *fp;
    char *filepath = argv[1];
    size_t len = 0;
    ssize_t read; 
    char *line = NULL;

    fp =  fopen(filepath, "r");
    if (fp == NULL){
        exit(1);
    }


    int t = 0;
    int c = 0;
    int a = 0;
    int g = 0;

    while ((read = getline(&line, &len, fp)) != -1) {
        int *counts = getCounts(line, strlen(line));
        a += counts[0];
        c += counts[1];
        g += counts[2];
        t += counts[3];
        free(counts);


    }

    printf("%d %d %d %d\n",a,c,g,t);
    free(line);
    fclose(fp);
    return 0;
}
