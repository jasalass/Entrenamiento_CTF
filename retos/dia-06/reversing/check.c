#include <stdio.h>
/* Imprime la flag aplicando la inversa. Entiende rotl8(d[i], 7) o ejecuta el binario. */
int main(void){
    unsigned char d[]={ 0x8c, 0x98, 0x82, 0x8e, 0xf6, 0xc8, 0x60, 0x6c, 0xbe, 0xe4, 0xca, 0xec, 0xca, 0xe4, 0xe6, 0xd2, 0xdc, 0xce, 0xbe, 0xe4, 0xea, 0xc8, 0xc6, 0xfa };
    int n=sizeof(d);
    for(int i=0;i<n;i++){
        unsigned char b=d[i]; unsigned char r=(unsigned char)((b<<7)|(b>>(8-7)));
        putchar(r);
    }
    putchar('\n');
    return 0;
}
