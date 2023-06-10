%{
    #include<stdio.h>
    #include<stdlib.h>
%}

%token LETTER DIGIT NL UND

%%

stmt : variabe NL { printf("Valid Variable\n"); exit(0); };
variabe : LETTER alphanumeric;
alphanumeric : LETTER alphanumeric
    | UND alphanumeric
    | DIGIT alphanumeric
    | LETTER 
    | DIGIT
    ;

%%

main()
{
    printf("\nEnter a variable : ");
    yyparse();
}
int yyerror(char *s)
{
    printf("\n%s\n",s);
    printf("\nInvalid variable\n");
    exit(0);
}