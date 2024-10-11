#include<stdio.h>
#include<string.h>

void main() {
char icode[10][30], str[20], opr[10];
int i = 0;

printf("\nEnter the set of intermediate code (terminated by 'exit'):\n");

do {
scanf("%s", icode[i]);
} while (strcmp(icode[i++], "exit") != 0);

printf("\nTarget code generation");
printf("\n*******************\n");

i = 0;
do {
strcpy(str, icode[i]);

switch (str[3]) {
case '+':
strcpy(opr, "ADD");
break;
case '-':
strcpy(opr, "SUB");
break;
case '*':
strcpy(opr, "MUL");
break;
case '/':
strcpy(opr, "DIV");
break;
default:
printf("\nUnknown operator in line: %s\n", str);
i++;
continue;
}

printf("\nMov\t%c, R%d", str[2], i);
printf("\n%s\t%c, R%d", opr, str[4], i);
printf("\nMov\tR%d, %c", i, str[0]);

} while (strcmp(icode[++i], "exit") != 0);

printf("\n");
}

/*
Enter the set of intermediate code (terminated by 'exit'):
A=b+c
D=f*k
X=A/D
exit

Target code generation
*******************

Mov     b, R0
ADD     c, R0
Mov     R0, A
Mov     f, R1
MUL     k, R1
Mov     R1, D
Mov     A, R2
DIV     D, R2
Mov     R2, X
*/
