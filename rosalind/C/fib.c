#include <stdio.h>
#include <stdlib.h>


int *calcRabbit(int n, int k){
    int pairs[40] = {1, 1};
    int *ret = malloc(sizeof(int));

    for(int i = 2; i < n; i++){
        int f1 = pairs[i-1];
        int f2 = pairs[i-2];
        printf("val: %d", f1+f2);
        pairs[i] = f1+f2;        
    }
    ret = pairs[n];
    return ret;
}

int main(int argc, char *argv[]){
    if(argc < 3){
        printf("Usage: ./fib n k\n");
        exit(1);
    }

    char *p;

    int k = strtol(argv[2], &p, 10);
    int n = strtol(argv[1], &p, 10);
    printf("K: %d\n", k);
    printf("N: %d\n", n);

    printf("%d", *calcRabbit(n, k));
}
