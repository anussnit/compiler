%{
  #include<stdio.h>
  int comment=0;
%}

%%
"//".*\n        {comment++;}
"/*"(.|\n)*"*/" { comment++;}
[\n\t]       {;}
#.* {printf("%s is a preprocessor directive\n",yytext);}
[+-]?[0-9]+(\.[0-9]+)?(E[+-]?[0-9]+) {printf("%s\tis a Exponet number\n",yytext);}
([+-]?[0-9]+)\.[0-9]+ {printf("%s \t is a floating number\n",yytext);}
[+-]?[0-9]+ { printf("%s\t is a number\n",yytext); }

(void|main|if|else|printf|int|float) {printf("%s\t is a reserved keyword\n",yytext);}
[a-zA-Z_][a-zA-Z0-9_]* { printf("%s \t is a identifier\n",yytext); }

[=*/+\-%] { printf("%s\tis a Arithmetic operator\n",yytext);}
(==|<|<=|>|>=|!=) { printf("%s\t is a relational operator\n",yytext);}
[(){};,] { printf("%s\t is a special operator\n",yytext);}
%%
int main(int argc, char**argv){
    yyin=fopen("input.c","r");
if(!yyin)
{
printf("could not open the file");
exit(0);
}
yylex();
fclose(yyin);
return(0);
}
int yywrap()
{return(1);}
