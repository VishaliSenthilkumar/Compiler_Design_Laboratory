%{
    #include<stdio.h>
    #include<stdlib.h>
%}

%token NUMBER
%left '+' '-'
%left '*' '/' '%'
%left '(' ')'

%%

ArithmeticExpression : E { printf("\nRESULT = %d\n", $$); return 0; };
E : E '+' E { $$ = $1 + $3 ; }
	| E '-' E { $$ = $1 - $3 ; }
	| E '*' E { $$ = $1 * $3 ; }
	| E '/' E { $$ = $1 / $3 ; }
	| E '%' E { $$ = $1 % $3 ; }
	| '('E')'  { $$ = $2 ; }
	| NUMBER { $$ = $1 ; }
	;

%%

void main()
{
    printf("\nEnter the arithmetic expression : \n");
    yyparse();
    printf("\nExpression is valid\n");
}

int yyerror()
{
    printf("\nExpression is invalid\n");
    exit(0);
}

int yywrap()
{
    return(1);
}