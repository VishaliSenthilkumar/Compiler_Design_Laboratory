%{
    #include<stdio.h>
    #include<stdlib.h>
%}

%token NUM ID
%left '+' '-'
%left '*' '/'

%%

expr : expr '+' expr
    | expr '-' expr
    | expr '*' expr
    | expr '/' expr
    | '-' NUM
    | '-' ID
    | '('expr')'
    | NUM
    | ID
    ;

%%

main()
{
    printf("\nEnter the expression: ");
    yyparse();
    printf("\nExpression is valid");
}
int yyerror(char *s)
{
    printf("\nExpression is invalid\n");
    exit(1);
}
