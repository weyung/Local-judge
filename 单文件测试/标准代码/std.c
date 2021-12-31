#include <stdio.h>
#define N 10
void inputarray(int *arr);
void handlearray(int *arr);
void outputarray(int *arr);
void swap(int *p,int *q);
int main()
{
    int array[N]= {0};
    inputarray(array);
    handlearray(array);
    outputarray(array);
    return 0;
}
void swap(int *p,int *q)
{
    int temp=*p;
    *p=*q;
    *q=temp;
}
void handlearray(int *arr)
{
    int min_index=0;    // the index of the minimum number 
    int min=arr[0];     // the minimum number
    for(int i=1;i<N;i++)
    {
        if(*(arr+i)<min)
        {
            min=*(arr+i);
            min_index=i;
        }
    }
    swap((arr+min_index),(arr+0));
    int max_index=0;    // the index of the maximum number 
    int max=arr[0];     // the maxinum number
    for(int i=1;i<N;i++)
    {
        if(*(arr+i)>max)
        {
            max=*(arr+i);
            max_index=i;
        }
    }
    swap((arr+max_index),(arr+9));
}
void inputarray(int *arr)
{
    for(int i=0; i<N; i++)
    {
        scanf("%d",(arr+i));
    }
}
void outputarray(int *arr)
{
    for(int i=0; i<N; i++)
    {
        printf("%d ",*(arr+i));
    }
}