#include<stdio.h>

void codechange(char *a, char *b){	//���¹���ʵ�ֽ��ļ���a�����ݴ����ļ���b����ȥ���ո�
	FILE *fp = fopen(a,"r");
	FILE *fp2 = fopen(b,"w");
	int i=0,j=0;
	i = fgetc(fp);
	while(i != EOF){
		j = fgetc(fp);
		if(i == '\n' && j == '\n');
		else{
			fputc(i,fp2);
		}
		i = j;
	}
} 

int main(){
	codechange("C:\\Users\\29624\\Desktop\\����������Ŀ\\����\\MyProject\\1.txt","3.txt"); //���Դ���
	 
} 
