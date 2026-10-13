#include <stdio.h>
/* Imprime la flag aplicando la inversa. Entiende (d[i] - prev) & 0xff  (prev = cifrado anterior, prev0 = 0x03) o ejecuta el binario. */
int main(void){
    unsigned char d[]={ 0x49, 0x95, 0xd6, 0x1d, 0x98, 0xfc, 0x2e, 0x63, 0xc2, 0x34, 0x99, 0x0f, 0x74, 0xe6, 0x59, 0xc2, 0x30, 0x97, 0xf6, 0x2d, 0x62, 0xdc, 0x48, 0xc5 };
    int n=sizeof(d);
    unsigned char prev=0x03;
    for(int i=0;i<n;i++){
        unsigned char p=(unsigned char)(d[i] - prev);
        putchar(p);
        prev=d[i];
    }
    putchar('\n');
    return 0;
}
