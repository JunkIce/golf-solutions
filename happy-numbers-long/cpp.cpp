// Bytes
#include<cstdio>
bool h(int n){bool y[1001]={};int u;while(!y[n]){if(n==1)return 1;y[n]=1;for(u=0;n;n/=10)u+=(n%10)*(n%10);n=u;}return 0;}int main(){for(int i=1;i<1001;i++)if(h(i))printf("%d\n",i);}
// --
// Chars
// (same as bytes)
