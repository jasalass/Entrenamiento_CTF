#include <stdio.h>
/* Imprime la flag aplicando la inversa. Entiende d[i] ^ prev  (prev = cifrado anterior, prev0 = 0xe2) o ejecuta el binario. */
int main(void){
    unsigned char d[]={ 0xa4, 0xe8, 0xa9, 0xee, 0x95, 0xf1, 0xc3, 0xf7, 0xa8, 0xda, 0xbf, 0xc9, 0xac, 0xde, 0xad, 0xc4, 0xaa, 0xcd, 0x92, 0xa4, 0xc2, 0xb7, 0x8f, 0xf2 };
    int n=sizeof(d);
    unsigned char prev=0xe2;
    for(int i=0;i<n;i++){
        unsigned char p=(unsigned char)(d[i] ^ prev);
        putchar(p);
        prev=d[i];
    }
    putchar('\n');
    return 0;
}
