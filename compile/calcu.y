%{
  
  #include<stdio.h>

  int flag=0;

%}

%token NUMBER

%left '+''-'
%left '*''/''%'
%left '('')'

%%

ArithmeticExpression: E{
  
  printf("\n Result=%d\n",$$);

  return 0;

};

E:E'+'E {$$=$1+$3;}
 |E'-'E {$$=$1-$3;}
 |E'*'E {$$=$1*$3;}
 |E'/'E {$$=$1/$3;}
 |E'%'E {$$=$2;}
 |'('E')' {$$=$2;}
 | NUMBER {$$=$1;}
;

%%

void main()
{
printf("\n enter any arithmetic expression which can have operations Addition, Subtraction, Multiplication, Division, Modulus and Round brackts:\n");

  yyparse();
  
  if(flag==0)
    
     printf("\n entered arithmetic expression is valid\n\n");
}

void yyerror()
{
  printf("\n entered arithmetic expression is invalid \n\n");
  flag=1;
}
