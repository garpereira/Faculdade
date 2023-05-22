#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <pthread.h>

void iniciaSint(int Sint[], int T[], char K[]){
    int i;
    int k = strlen(K);
    for(i=0;i<2000;i++){
        Sint[i] = i;
        T[i] = K[i%k];
    }
}

void swap(int *Si, int *Sj){
    int k = *Si;
    *Si = *Sj;
    *Sj = k;
}

void cript2(char K[], char S[], unsigned char buffer[]){
    int Sint[2000];
    int T[2000];
    unsigned char *output;//[2000];
    output = (unsigned char*)malloc(sizeof(unsigned char)*2000);
    int tamS = strlen(S);

    printf("descriptografando....\n");

    iniciaSint(Sint, T, K);
    int i , j, k, t, l;
    j = 0;
    for(i=0;i<2000;i++){
        j =(j+Sint[i]+T[i])%2000;
        swap(&Sint[i], &Sint[j]);
    }
    
    i = j = 0;
    l = k = t = 0;

    while(l < 2000){
        i = (i+1)%2000;
        j = (j+Sint[i])%2000;
        swap(&Sint[i], &Sint[j]);

        t = (Sint[i]+Sint[j])%2000;
        k = Sint[t];
        output[l] = S[l]^k;
        l++;
    }

    // for(i=0;i<tamS;i++)
    //     buffer[i] = output[i];

    //strcpy(buffer, output);
    printf("%s\n", buffer);
    
    FILE *arquivo;
    arquivo = fopen("chatLOG.txt", "a");
    for(i=0;i<tamS;i++){
        fprintf(arquivo, "%02x:",output[i]);
    }
    fprintf(arquivo, "%s", "\n");
    fclose(arquivo);
}

void cript(char K[], char S[], unsigned char buffer[]){
    int Sint[2000];
    int T[2000];
    unsigned char *output;//[2000];
    output = (unsigned char*)malloc(sizeof(unsigned char)*2000);
    int tamS = strlen(S);

    iniciaSint(Sint, T, K);
    int i , j, k, t, l;
    j = 0;
    for(i=0;i<2000;i++){
        j =(j+Sint[i]+T[i])%2000;
        swap(&Sint[i], &Sint[j]);
    }
    
    i = j = 0;
    l = k = t = 0;

    while(l < 2000){
        i = (i+1)%2000;
        j = (j+Sint[i])%2000;
        swap(&Sint[i], &Sint[j]);

        t = (Sint[i]+Sint[j])%2000;
        k = Sint[t];
        output[l] = S[l]^k;
        l++;
    }

    // for(i=0;i<tamS;i++)
    //     buffer[i] = output[i];

    strcpy(buffer, output);
    
    printf("%s\n", buffer);
    
    FILE *arquivo;
    arquivo = fopen("chatLOG.txt", "a");
    for(i=0;i<tamS;i++){
        fprintf(arquivo, "%02x:",output[i]);
    }
    fprintf(arquivo, "%s", "\n");
    fclose(arquivo);

    cript2(K, buffer, buffer);
}


int main(int argc, char **argv){
    char S[256];
    char K[256];
    int Sint[256];
    int T[256];

    //int output[256];
    unsigned char output[256];

    scanf("%s", S);
    scanf(" %s", K);

    iniciaSint(Sint, T, K);
    int i , j, k, t, l;
    j = 0;
    for(i=0;i<256;i++){
        j =(j+Sint[i]+T[i])%256;
        swap(&Sint[i], &Sint[j]);
    }
    
    i = j = 0;
    l = k = t = 0;

    while(l < 256){
        i = (i+1)%256;
        j = (j+Sint[i])%256;
        swap(&Sint[i], &Sint[j]);

        t = (Sint[i]+Sint[j])%256;
        k = Sint[t];
        output[l] = S[l]^k;
        l++;
    }

    for(i=0;i<strlen(S);i++){
        printf("%x:",output[i]);
    }
    return 0;
}