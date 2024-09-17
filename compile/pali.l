%{
    #include<stdio.h>
    int i,j,flag;

%}


%%

[a-zA-Z0-9]+ {

     for (i=0,j=yyleng-1;i<=j;i++,j--) {
         if (yytext[i] == yytext[j]) {
               flag =1;
             }
         else {
              flag=0;
              break;
              }
          }
	  if (flag ==1)
	      printf("given string is palindrome");
	  else
	      printf("Given string is not palindrome");
                 }

%%

    int main()
{
     printf("enter a string :");
     yylex();
     return 0;
}

int yywrap()
{
    return 1;
}  
