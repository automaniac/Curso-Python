#include <stdio.h>

int main(){
    char palavra[] = "mundo";
    for(int i=strlen(palavra)-1; i>=0; i--){
        printf("%c", palavra[i]);
    }
}