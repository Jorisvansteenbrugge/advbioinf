#include <stdio.h>
#include <stdlib.h>


int calcRabbit(int n, int k){
    long int pairs[40] = {1, 1};
    //int *ret = malloc(sizeof(int));

    for(int i = 2; i < n; ++i){
        long int f1 = pairs[i-1];
        long int f2 = pairs[i-2] * 3;
        long int summ = (f1+f2);
        pairs[i] = summ;
             
    }
    return pairs[n-1];
}

int main(int argc, char *argv[]){
    if(argc < 3){
        printf("Usage: ./fib n k\n");
        exit(1);
    }

    char *p;

    int k = strtol(argv[2], &p, 10);
    int n = strtol(argv[1], &p, 10);


    printf("%d\n", calcRabbit(n, k));

    return 0;
}
