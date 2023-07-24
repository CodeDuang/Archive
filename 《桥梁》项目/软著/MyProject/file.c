#include<stdio.h>

void codechange(char *a, char *b){	//以下功能实现将文件名a的内容传入文件名b，且去掉空格
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
	codechange("C:\\Users\\29624\\Desktop\\《桥梁》项目\\软著\\MyProject\\1.txt","3.txt"); //测试代码
	 
} 
