//
//  main.cpp
//  test14
//
//  Created by 王早8⃣️ on 2021/12/26.
//

#include <iostream>

int main()
{
    void input(int array[],int n);
    void exchange(int array[],int n);
    void output(int array[],int n);
    int a[10];
    input(a,10);                                               //调用输入函数
    exchange(a,10);                                            //调用交换函数
    output(a,10);                                              //调用输出函数
    return 0;
}

void input(int array[],int n)                                  //输入函数
{
    int i,*p;p=array;
    printf("please enter 10 integer numbers\n");
    for(i=0;i<n;i++,p++)
        scanf("%d",p);
}

void exchange(int array[],int n)                               //交换函数
{
    int *max,*min,*p,temp1,temp2;
    p=max=min=array;
    for(p=array+1;p<array+n;p++)
    {
        if(*p>*max)
            max=p;                                             //将max指向p所指向的大数
        else if(*p<*min)
            min=p;                                             //将min指向p所指向的小数
    }
    temp1=array[0];array[0]=*min;*min=temp1;                   //将小数交换给数组第一个数
    if(max==array)max=min;                                     //第一个数为最大数
    temp2=array[n-1];array[n-1]=*max;*max=temp2;
}

void output(int array[],int n)                                 //输出函数
{
    int *p;
    p=array;
    printf("the exchanged array is:\n");
    for(p=array;p<array+n;p++)
        printf("%d\t",*p);
    printf("\n");
}
