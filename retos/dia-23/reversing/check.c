#include <stdio.h>
/* Imprime la flag aplicando la inversa. Entiende (rotr8(d[i], 4) - 4) & 0xff o ejecuta el binario. */
int main(void){
    unsigned char d[]={ 0xa4, 0x05, 0x54, 0xb4, 0xf7, 0x86, 0x63, 0x73, 0x36, 0x67, 0x96, 0xa7, 0x96, 0x67, 0x77, 0xd6, 0x27, 0xb6, 0x36, 0xe7, 0x56, 0x67, 0x87, 0x18 };
    int n=sizeof(d);
    for(int i=0;i<n;i++){
        unsigned char b=d[i]; unsigned char r=(unsigned char)((b>>4)|(b<<(8-4)));
        putchar((unsigned char)(r - 4));
    }
    putchar('\n');
    return 0;
}
