#include <iostream>
#include <ctime>

using namespace std;



void voidNull(){;}


class FuncPair{
public:
    FuncPair* FuncPairNull(){;}
    int count = 0;
    int dT = 0;
//    void (*f)() = voidNull;
    FuncPair* (*f)() = (FuncPair*(*)())&FuncPairNull;
    FuncPair(){;}
    FuncPair(int c, int dt, FuncPair* (*Function)()) {
        this->count = c;
        this->dT = dt;
        this->f = Function;
//        this->r = Return;
    }
    operator =(FuncPair a){
        this->count = a.count;
        this->dT = a.dT;
        this->f = a.f;
//        this->r = a.r;
    }
    FuncPair* exec(){
//        this->f();
        return this->f();
    }
};

class Return
{
public:
    FuncPair* (*ret)() = (FuncPair*(*)())&FuncPair::FuncPairNull;
    Return() {;}
    Return(FuncPair* (*Ret)()){
        this->ret = Ret;
    }
    FuncPair* exec(){
        return this->ret();
    }
};

class doOnTimer
{
    doOnTimer null(){;}
public:
    int count = 0;
    long int dT = 0;
    int clocks = 0;
    FuncPair func = FuncPair();

    doOnTimer(){
        ;
    }
    doOnTimer(FuncPair f) {
        this->count = f.count;
        this -> dT = f.dT/CLOCKS_PER_SEC;
        this->clocks = f.dT%CLOCKS_PER_SEC;
        this -> func = f;
    }
    operator =(doOnTimer* a){
        this -> dT = a->dT;
        this->clocks = a->clocks;
        this -> func = a->func;
    }
    void set(int dt, FuncPair f){
        this -> dT = dt/CLOCKS_PER_SEC;
        this->clocks = dt%CLOCKS_PER_SEC;
        this -> func = f;
    }
    doOnTimer* Execute(){
        FuncPair *tmp = this->func.exec();
        int tmp2 = tmp[0].count;
        doOnTimer *A = new doOnTimer[tmp2];
        for (int i = 0; i<tmp2; i++){
            A[i] = doOnTimer(tmp[i]);
        }
        delete(tmp);
        return A;
    }
};

class Conveyer
{

public:
    int len = 0;
    long int prevT = clock();
    doOnTimer *A = new doOnTimer[len];

    Conveyer() {
        this->len = 0;
        this->A = new doOnTimer[len];
        this->prevT = clock();
    }
    ~Conveyer() {
        delete(this->A);
    }
    void add(doOnTimer a){
        this->len+=1;
        doOnTimer *B = new doOnTimer[len];
        for (int i = 0; i<len-1; i++){
            B[i]=this->A[i];
        }
        B[this->len-1]=a;
        delete(this->A);
        this->A = B;
    }
    void remove(int i){
        doOnTimer *B = new doOnTimer[len-1];
        for (int j = 0; j<i; j++){
            B[j] = this->A[j];
        }
        for (int j = i; j<this->len-1; j++){
            B[j] = this->A[j+1];
        }
        delete(this->A);
        this->A = B;
        this->len--;
    }
    void Execute(){
        int tmpT = clock();
        int dT = (tmpT - this->prevT);
        for (int i = 0; i<this->len; i++){
            if (A[i].dT < 0){
                doOnTimer *tmp = this->A[i].Execute();
                int tmp2 = tmp[0].count;
                for (int i = 0; i<tmp2; i++){
                    this->add(tmp[i]);
                }
                delete(tmp);
                this->remove(i);
            } else {
                this->A[i].clocks-=dT;
                if (this->A[i].clocks<0){
                    this->A[i].dT-=1;
                    this->A[i].clocks+=CLOCKS_PER_SEC;
                }
            }
        }
        this->prevT = tmpT;
    }
};



Return *R = new Return[4];



FuncPair* f1(){
    cout << "0 ";
    return R[0].ret();
}
FuncPair* f2(){
    cout << "00 ";
    return R[1].ret();
}
FuncPair* f3(){
    cout << "000 ";
    return R[2].ret();
}
FuncPair* f4(){
    cout << "0000 ";
    return R[3].ret();
}



FuncPair* r1(){
    FuncPair *A = new FuncPair[2];
    A[0] = FuncPair(2, 1*CLOCKS_PER_SEC, f2);
    A[1] = FuncPair(2, 1*CLOCKS_PER_SEC, f4);
    cout << "ret 1" << endl;
    return A;
}
FuncPair* r2(){
    FuncPair *A = new FuncPair[1];
    A[0] = FuncPair(1, 1*CLOCKS_PER_SEC, f3);
    cout << "ret 2" << endl;
    return A;
}
FuncPair* r3(){
    FuncPair *A = new FuncPair[1];
    A[0] = FuncPair(1, 1*CLOCKS_PER_SEC, f4);
    cout << "ret 3" << endl;
    return A;
}
FuncPair* r4(){
    FuncPair *A = new FuncPair[1];
    A[0] = FuncPair(1, 1*CLOCKS_PER_SEC, f1);
    cout << "ret 4" << endl;
    return A;
}

int main()
{
    R[0].ret = r1;
    R[1].ret = r2;
    R[2].ret = r3;
    R[3].ret = r4;
    Conveyer B = Conveyer();
    B.add(doOnTimer(FuncPair(1, 1*CLOCKS_PER_SEC, f1)));
    while (1){
        B.Execute();
    }
    return 0;
}


