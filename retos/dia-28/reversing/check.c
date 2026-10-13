#include <stdio.h>
/* Imprime la flag aplicando la inversa. Entiende (d[i] - prev - 98) & 0xff  (prev = cifrado anterior, prev0 = 0x09) o ejecuta el binario. */
int main(void){
    unsigned char d[]={ 0xb1, 0x5f, 0x02, 0xab, 0x88, 0x4e, 0xe2, 0x7c, 0x3d, 0x11, 0xd8, 0xb0, 0x77, 0x4b, 0x20, 0xeb, 0xbb, 0x84, 0x45, 0x17, 0xb2, 0x78, 0x45, 0x24 };
    int n=sizeof(d);
    unsigned char prev=0x09;
    for(int i=0;i<n;i++){
        unsigned char p=(unsigned char)(d[i] - prev - 98);
        putchar(p);
        prev=d[i];
    }
    putchar('\n');
    return 0;
}
