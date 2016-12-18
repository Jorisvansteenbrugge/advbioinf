#include <stdio.h>
#include <stdlib.h>

int * getCounts(char *dna, int dnalen){
    int t = 0;
    int c = 0;
    int a = 0;
    int g = 0;
    int *counts = malloc(5* sizeof(int));
    printf("len %d\n", dnalen);
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

            //default:
             //   printf("\n%c\n", nuc);
              //  counts[0] = a;
              //  counts[1] = c;
              //  counts[2] = g;
              //  counts[3] = t;
              //  return counts;
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
    const int buffsize = 1000;
    char *filepath = argv[1];
    char buff[buffsize];
    

    fp =  fopen(filepath, "r");
    fscanf(fp, "%999s", buff);

    printf("%s\n", buff);   
    int dnalen = sizeof(buff) / sizeof(int);

    int *counts = getCounts(buff, dnalen);
    printf("%d %d %d %d\n",counts[0], counts[1], counts[2], counts[3]);
    
    free(counts); 
    return 0;
}
