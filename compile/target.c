#include<stdio.h>
#include<string.h>
char op[2],arg1[5],arg2[5],result[5];
void main()
{
FILE *fp1, *fp2;
fp1=fopen("inputt.txt","r");
fp2=fopen("outputt.txt","w");
fscanf(fp1,"%s%s%s%s",op,arg1,arg2,result);
while(!feof(fp1))
{
if(strcmp(op,"+")==0)
{
fprintf(fp2,"\nMOV RO ,%s",arg1);
fprintf(fp2,"\n ADD RO,%s",arg2);
fprintf(fp2,"\nMOV %s,RO",result);
}
if(strcmp(op,"*")==0)
{
fprintf(fp2,"\nMOV RO,%s",arg1);
fprintf(fp2,"\nMUL RO,%s",arg2);
fprintf(fp2,"\nMOV %s,R0",result);
}
if(strcmp(op,"-")==0)
{
fprintf(fp2,"\nMOV RO,%s",arg1);
fprintf(fp2,"\nSUB RO,%s",arg2);
fprintf(fp2,"\nMOV %s,RO",result);
}
if(strcmp(op,"/")==0)
{
fprintf(fp2,"\nMOV RO,%s",arg1);
fprintf(fp2,"\nDIV RO,%s",arg2);
fprintf(fp2,"\nMOV %s,RO",result);
}
if(strcmp(op,"=")==0)
{
fprintf(fp2,"\nMOV RO,%s",arg1);
fprintf(fp2,"\nMOV %s,RO",result);
}
fscanf(fp1,"%s%s%s%s",op,arg1,arg2,result);
}
fclose(fp1);
fclose(fp2);
}

