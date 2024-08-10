%{
#include<stdio.h>
  int vowel=0,consonants=0;
%}

%%
[aeiuoAEIOU] {printf("\n %s is vowel",yytext); vowel++;}
[a-zA-Z] {printf("\n %s is consonant",yytext);consonants++;}
%%

int yywrap()
{
return 1;
}
int main()
{
printf("\n enter the string : when done press crt+d to view output\n");
yylex();
yywrap();
printf("\n the number of vowels in the string is %d\n",vowel);
printf("\n the number of consonants in the string is %d \n ",consonants);
return 0;
}
