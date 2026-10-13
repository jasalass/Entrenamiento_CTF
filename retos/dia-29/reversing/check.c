#include <stdio.h>
/* Imprime la flag aplicando la inversa. Entiende ((d[i] - 46) & 0xff) ^ prev  (prev = cifrado anterior, prev0 = 0x66) o ejecuta el binario. */
int main(void){
    unsigned char d[]={ 0x4e, 0x30, 0x9f, 0x06, 0xab, 0xfd, 0xfd, 0xf2, 0xdb, 0xd7, 0xe0, 0xc4, 0xcf, 0xeb, 0xc6, 0xdd, 0xe1, 0xb4, 0x19, 0x9e, 0x20, 0x7b, 0x76, 0x39 };
    int n=sizeof(d);
    unsigned char prev=0x66;
    for(int i=0;i<n;i++){
        unsigned char t=(unsigned char)(d[i] - 46);
        unsigned char p=(unsigned char)(t ^ prev);
        putchar(p);
        prev=d[i];
    }
    putchar('\n');
    return 0;
}
