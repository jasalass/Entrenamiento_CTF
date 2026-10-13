#include <stdio.h>
/* Imprime la flag aplicando la inversa. Entiende (d[i] + prev) & 0xff  (prev = cifrado anterior, prev0 = 0xde) o ejecuta el binario. */
int main(void){
    unsigned char d[]={ 0x68, 0xe4, 0x5d, 0xea, 0x91, 0xd3, 0x5f, 0xd7, 0x88, 0xea, 0x7b, 0xfb, 0x6a, 0x08, 0x6b, 0xfe, 0x70, 0xf7, 0x68, 0x0f, 0x54, 0x13, 0x54, 0x29 };
    int n=sizeof(d);
    unsigned char prev=0xde;
    for(int i=0;i<n;i++){
        unsigned char p=(unsigned char)(d[i] + prev);
        putchar(p);
        prev=d[i];
    }
    putchar('\n');
    return 0;
}
