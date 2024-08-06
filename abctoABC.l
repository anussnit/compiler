%{
#include<stdio.h>
%}

%%
"abc" { printf("ABC"); }
.     { printf("%c",yytext[0]); }
 \n    { printf("\n"); }
%%

int yywrap() {
  return 1;
}

int main() {
  yylex();
  return 0;
  }
