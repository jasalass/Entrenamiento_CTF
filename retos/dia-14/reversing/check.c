#include <stdio.h>
/* Imprime la flag aplicando la inversa. Entiende rotr8(d[i], 5) ^ (i & 0xff) o ejecuta el binario. */
int main(void){
    unsigned char d[]={ 0xc8, 0xa9, 0x68, 0x88, 0xef, 0x2c, 0xe6, 0x66, 0xea, 0x6f, 0xed, 0xaf, 0x2d, 0xef, 0xaf, 0xcc, 0xcf, 0xce, 0xa9, 0x64, 0x2c, 0xcc, 0xac, 0x4d };
    int n=sizeof(d);
    for(int i=0;i<n;i++){
        unsigned char b=d[i]; unsigned char r=(unsigned char)((b>>5)|(b<<(8-5)));
        putchar((unsigned char)(r ^ (i & 0xff)));
    }
    putchar('\n');
    return 0;
}
