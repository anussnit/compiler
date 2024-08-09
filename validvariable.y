%{
  
  #include<stdio.h>

  int valid=1;

%}

%token digit letter

%%

 start : letter s

 s : letter s
   
    | digit s

    |  
 
    ;

%%

int yyerror()
{
  printf("\n its not a identifier \n");
  valid=0;
  return 0;
}


int main()
{
  printf("\n enter a name to tested for identifie ");
  yyparse();
  if(valid)
  {
       printf("\n It is identifier\n");
  }
}
