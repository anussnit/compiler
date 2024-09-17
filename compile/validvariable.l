%{

  #include "y.tab.h"

%}

%%

[a-zA-Z_][a-zA-Z_0-9]* return letter;

[0-9]       return digit;

.         return yytext[0];

\n          return 0;


%%

int yywrap()

{

return 1;

}

/*

yacc -d validvariable.y
ssnit@ssnit-ThinkCentre-E73:~/com$ flex validvariable.l
ssnit@ssnit-ThinkCentre-E73:~/com$ gcc y.tab.c lex.yy.c -ll -w
ssnit@ssnit-ThinkCentre-E73:~/com$ ./a.out

*/
