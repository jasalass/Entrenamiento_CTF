#include <stdio.h>
/* Imprime la flag aplicando la inversa. Entiende rotr8(d[i], 3) o ejecuta el binario. */
int main(void){
    unsigned char d[]={ 0x32, 0x62, 0x0a, 0x3a, 0xdb, 0x23, 0x81, 0xa9, 0xfa, 0x93, 0x2b, 0xb3, 0x2b, 0x93, 0x9b, 0x4b, 0x73, 0x3b, 0xfa, 0x83, 0x93, 0x9b, 0x6b, 0xeb };
    int n=sizeof(d);
    for(int i=0;i<n;i++){
        unsigned char b=d[i]; unsigned char r=(unsigned char)((b>>3)|(b<<(8-3)));
        putchar(r);
    }
    putchar('\n');
    return 0;
}
