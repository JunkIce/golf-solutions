// Bytes
#include <stdio.h>#include <stdbool.h>bool h(int n){bool c[1001]={0};bool y[1001]={0};int u,d;while(n!=1&!y[n]){if(c[n])return c[n];y[n]=1;u=0;for(int x=n;x;x/=10)u+=(d=x%10)*d;n=u;}return c[n] = n == 1;}int main(){for(int i=1;i<1001;i++)if(h(i))printf("%d\n",i);}
// --
// Chars
// (same as bytes)
