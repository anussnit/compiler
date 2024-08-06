%{
#include<stdio.h>
int line=0,chars=0,words=0,spaces=0;
%}

%%

\n    {line++;}

\t    {spaces+=4;}

[ ]   {spaces++;}

[^ \t\n#]+    {words++;chars+=yyleng;}  

#   { return 0;}

%%

int yywrap()

{


      return 1;


}


int main()

{
  
     printf("Enter the string\n");
     yylex();
     printf("Lines:%d\nWords:%d\nChars:%d\nSpaces:%d\n",line,words,chars,spaces);
   return 0;

}

// Con ^ D output
