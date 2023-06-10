%{
int comment = 0;
%}

identifier [a-zA-Z][a-zA-Z0-9]*
constant [0-9]+

%%

#.* { if(!comment) printf("\n%s is a preprocessor directive ", yytext); }
int |
char | 
float | 
double | 
while | 
for |
struct | 
typedef | 
do | 
if | 
break | 
continue | 
void | 
switch | 
return | 
else | 
goto { printf("\n%s is a keyword",yytext); }
"/*" { comment=1; printf("\n%s is a comment",yytext); }
{identifier} { if(!comment)printf("\n%s is a identifier",yytext); }
\{ { if(!comment) printf("\nBLOCK BEGINS"); }
\} { if(!comment) printf("\nBLOCK ENDS"); }
{identifier}\(.*\)  { if(!comment) printf("\n%s is a function", yytext); }
\) {printf("\n");}
\".*\"  { if(!comment) printf("\n%s is a string",yytext); }
{constant}  { if(!comment) printf("\n%s is a constant",yytext); }
\+\+ { if(!comment) printf("\n%s is a increment operator",yytext); }
-- { if(!comment) printf("\n%s is a decrement operator",yytext); }
= |
\+= |
-= |
\*= |
\/= |
%= { if(!comment) printf("\n%s is a assignment operator",yytext); }
\+ |
- |
\* |
\/ |
% { if(!comment) printf("\n%s is a arithmetic operator",yytext); }
\< |
\> |
\<= |
\>= |
== { if(!comment) printf("\n%s is a relational operator",yytext); }
, |
; ECHO;

%%

int main(int argc, char **argv)
{
    FILE *file;
    file = fopen("var.c","r");
    if(!file)
    {
        printf("File can't be opened\n");
        exit(0);
    }
    yyin = file;
    yylex();
    printf("\n");
    return(0);
}
int yywrap()
{
    return(1);
}