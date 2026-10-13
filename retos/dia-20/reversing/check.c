#include <stdio.h>
/* Imprime la flag aplicando la inversa. Entiende rotr8(d[i] ^ 0x65, 4) o ejecuta el binario. */
int main(void){
    unsigned char d[]={ 0x01, 0xa1, 0x71, 0x11, 0xd2, 0x23, 0x46, 0x66, 0x90, 0x42, 0x33, 0x02, 0x33, 0x42, 0x52, 0xf3, 0x83, 0x13, 0x90, 0x36, 0x26, 0xe6, 0x06, 0xb2 };
    int n=sizeof(d);
    for(int i=0;i<n;i++){
        unsigned char t=(unsigned char)(d[i] ^ 0x65);
        unsigned char r=(unsigned char)((t>>4)|(t<<(8-4)));
        putchar(r);
    }
    putchar('\n');
    return 0;
}
