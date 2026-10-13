#include <stdio.h>
/* Imprime la flag aplicando la inversa. Entiende rotr8(d[i], 7) ^ prev  (prev = cifrado anterior, prev0 = 0xa4) o ejecuta el binario. */
int main(void){
    unsigned char d[]={ 0x71, 0x9e, 0xef, 0x54, 0x97, 0xf9, 0x65, 0xaa, 0xfa, 0x44, 0x90, 0x73, 0x0b, 0xbc, 0xe7, 0x47, 0x94, 0xf9, 0x53, 0x9d, 0x7e, 0x8c, 0x75, 0x04 };
    int n=sizeof(d);
    unsigned char prev=0xa4;
    for(int i=0;i<n;i++){
        unsigned char b=d[i]; unsigned char r=(unsigned char)((b>>7)|(b<<(8-7)));
        unsigned char p=(unsigned char)(r ^ prev);
        putchar(p);
        prev=d[i];
    }
    putchar('\n');
    return 0;
}
