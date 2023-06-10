#include<iostream>
using namespace std;
int main()
{
    string icode[10], str="", opr="";
    int i=0;
    printf("Enter the intermediate code thats end with exit : \n");
    getline(cin,str);
    while(str!="exit")
    {
        icode[i]=str;
        i++;
//      getline(cin,str);
        cin>>str;
    }
    int j=0, n=i;
    for(i=0;i<n;i++)
    {
        str=icode[i];
        switch(str[3])
        {
            case '+' :
                opr = "ADD";
                break;
            case '-' :
                opr = "SUB";
                break;
            case '*' :
                opr = "MUL";
                break;
            case '/' :
                opr = "DIV";
                break;
        }
        cout<<"\nMOV "<<str[2]<<", R"<<j<<endl;
        cout<<opr<<" "<<str[4]<<", R"<<j<<endl;
        cout<<"MOV "<<"R"<<j<<", "<<str[0]<<endl;
        j++;
    }
    return 0;
}
