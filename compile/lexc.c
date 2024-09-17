#include<stdio.h>
#include<ctype.h>
#include<string.h>
int main()
{
FILE *input,*output;
int l=1;
int t=0;
int j=0;
int i,flag;
char ch,str[20];
input=fopen("input.c","r");
output=fopen("output.txt","w");
char keyword[30][30]={"int","main","if","else","do","while"};
while(!feof(input))
{
i=0;
flag=0;
ch=fgetc(input);
if(ch=='+' || ch=='-' || ch=='*' || ch=='/' || ch=='<' || ch=='>')
{
printf("%c is a operator \n",ch);
t++;
}
else if(ch==';' || ch=='{' || ch=='}' || ch=='(' || ch==')' || ch=='@' || ch=='!' || ch=='%')
{
printf("%c is a special symbol \n",ch);
t++;
}
else if(isdigit(ch))
{
printf("%c is a digit \n",ch);
t++;
}
else if(isalpha(ch))
{
str[i]=ch;
i++;
ch=fgetc(input);
while(isalnum(ch) && ch!=' ')
{
str[i]=ch;
i++;
ch=fgetc(input);
}
str[i]='\0';
for(j=0;j<=30;j++)
{
if(strcmp(str,keyword[j])==0)
{
flag=1;
break;
}}
if(flag==1)
{
printf("%s is a keyword \n",str);
i++;
}
else
{
printf("%s is a identifier \n",str);
t++;
}
}
else if(ch=='\n')
{
l++;
}
}
fclose(input);
fclose(output);
return 0;
}

