/*
ID: whuan2001
PROG: stamps
LANG: C++
*/
#include <stdio.h>
#define ITF 0x7FFFFFFF
FILE *fi,*fo;

long k,n;
long value[51];
long F[2000000];

inline long min(long a,long b)
{
    return a<b?a:b;
}

int main()
{
    long i,j,pmin;
    fi=fopen("stamps.in","r");
    fo=fopen("stamps.out","w");
    fscanf(fi,"%ld%ld",&k,&n);
    for (i=1;i<=n;i++)
        fscanf(fi,"%ld",&value[i]);
    F[i=0]=0;
    while (F[i]<=k)
    {
        i++;pmin=ITF;
        for (j=1;j<=n;j++)
            if (i-value[j]>=0)
                pmin=min(pmin,F[i-value[j]]);
        F[i]=pmin+1;
    }
    fprintf(fo,"%ld\n",i-1);
    fclose(fi);
    fclose(fo);
    return 0;
}
