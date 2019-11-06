
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

class Figure
{
public:

    char skin;
    int _8;
    int _9;
    int _6;
    int _3;
    int _2;
    int _1;
    int _4;
    int _7;

    Figure(char A);
    Figure();
};

Figure::Figure(char A) {
    skin=A;
    _8=0;
    _9=0;
    _6=0;
    _3=0;
    _2=0;
    _1=0;
    _4=0;
    _7=0;
}

Figure::Figure()
{
    skin='#';
    _8=0;
    _9=0;
    _6=0;
    _3=0;
    _2=0;
    _1=0;
    _4=0;
    _7=0;
}

class Player
{
public:
    char skin;
    bool active;
    int numerator;
    int leaderboardPos;
    Player() {
        this->skin = '#';
        this->active = 0;
        this->numerator = -1;
        this->leaderboardPos = 50;
    }
    void print(){
        cout << (this->numerator+1) << "-" << this->skin;
        if (this->leaderboardPos!=50) {cout << "   " << (this->leaderboardPos+1);}
        else {cout << "   " << '-';}
    }
};

class Field
{
public:

    Figure A[50][50];
    int X;
    int Y;

    Field(int x, int y);
    void Print(Player B[], int count, int term);
    void Move(int X, int Y, Player B);
    bool Check(int X, int Y, int winLenghth);
    bool End();
};

Field::Field(int x, int y) {
    this->X=x;
    this->Y=y;
    for(int i = 0; i < x; i++){
        for(int j = 0; j < y; j++){
            this->A[i][j].skin='_';
        }
    }
}

void Field::Print(Player B[], int count, int term)
{
    system("cls");
    cout << "  X:";
    for(int k = 0; k < this->X; k++){
        if (k<26) {cout << char(k+65) << ' ';}
        else {cout << char(k+71) << ' ';}
    }
    cout << "                       Players";
    cout << endl;
    for(int i = 0; i < this->Y; i++){
        if (i==0) {cout << "Y:" ;} else {cout << "  " ;}
        if (i<26) {cout << char(i+65) << '-';}
        else {cout << char(i+71) << '-';}
        for(int j = 0; j < this->X; j++){
            cout << this->A[j][i].skin << ' ';
        }
        cout << "               ";
        if (i == term) {cout << ":||:=--   ";} else {cout << "          ";}
        if (i<count) B[i].print();
        cout << endl;
    }
}

void Field::Move(int X, int Y, Player B)
{
    this->A[X][Y].skin=B.skin;
}

bool Field::Check(int X, int Y, int winLenghth)
{
    int tmp_8=0, tmp_9=0, tmp_6=0, tmp_3=0, tmp_2=0, tmp_1=0, tmp_4=0, tmp_7=0, tmp_X, tmp_Y;
    char tmp_C = this->A[X][Y].skin;

    for (int i = 1; i<winLenghth; i++){
        if (i!=0){
            tmp_X = X;
            tmp_Y = Y+i;
            if (!(tmp_X<0 or tmp_X>=this->X or tmp_Y<0 or tmp_Y>=this->Y)){
                if (tmp_C==this->A[tmp_X][tmp_Y].skin){
                    this->A[tmp_X][tmp_Y]._8++;
                    tmp_8++;
                    if (this->A[tmp_X][tmp_Y]._8>winLenghth-2) return 1;
                }
            }
        }
    }

    for (int i = 1; i<winLenghth; i++){
        if (i!=0){
            tmp_X = X+i;
            tmp_Y = Y+i;
            if (!(tmp_X<0 or tmp_X>=this->X or tmp_Y<0 or tmp_Y>=this->Y)){
                if (tmp_C==this->A[tmp_X][tmp_Y].skin){
                    this->A[tmp_X][tmp_Y]._9++;
                    tmp_9++;
                    if (this->A[tmp_X][tmp_Y]._9>winLenghth-2) return 1;
                }
            }
        }
    }

    for (int i = 1; i<winLenghth; i++){
        if (i!=0){
            tmp_X = X+i;
            tmp_Y = Y;
            if (!(tmp_X<0 or tmp_X>=this->X or tmp_Y<0 or tmp_Y>=this->Y)){
                if (tmp_C==this->A[tmp_X][tmp_Y].skin){
                    this->A[tmp_X][tmp_Y]._6++;
                    tmp_6++;
                    if (this->A[tmp_X][tmp_Y]._6>winLenghth-2) return 1;
                }
            }
        }
    }

    for (int i = 1; i<winLenghth; i++){
        if (i!=0){
            tmp_X = X+i;
            tmp_Y = Y-i;
            if (!(tmp_X<0 or tmp_X>=this->X or tmp_Y<0 or tmp_Y>=this->Y)){
                if (tmp_C==this->A[tmp_X][tmp_Y].skin){
                    this->A[tmp_X][tmp_Y]._3++;
                    tmp_3++;
                    if (this->A[tmp_X][tmp_Y]._3>winLenghth-2) return 1;
                }
            }
        }
    }

    for (int i = 1; i<winLenghth; i++){
        if (i!=0){
            tmp_X = X;
            tmp_Y = Y-i;
            if (!(tmp_X<0 or tmp_X>=this->X or tmp_Y<0 or tmp_Y>=this->Y)){
                if (tmp_C==this->A[tmp_X][tmp_Y].skin){
                    this->A[tmp_X][tmp_Y]._2++;
                    tmp_2++;
                    if (this->A[tmp_X][tmp_Y]._2>winLenghth-2) return 1;
                }
            }
        }
    }

    for (int i = 1; i<winLenghth; i++){
        if (i!=0){
            tmp_X = X-i;
            tmp_Y = Y-i;
            if (!(tmp_X<0 or tmp_X>=this->X or tmp_Y<0 or tmp_Y>=this->Y)){
                if (tmp_C==this->A[tmp_X][tmp_Y].skin){
                    this->A[tmp_X][tmp_Y]._1++;
                    tmp_1++;
                    if (this->A[tmp_X][tmp_Y]._1>winLenghth-2) return 1;
                }
            }
        }
    }

    for (int i = 1; i<winLenghth; i++){
        if (i!=0){
            tmp_X = X-i;
            tmp_Y = Y;
            if (!(tmp_X<0 or tmp_X>=this->X or tmp_Y<0 or tmp_Y>=this->Y)){
                if (tmp_C==this->A[tmp_X][tmp_Y].skin){
                    this->A[tmp_X][tmp_Y]._4++;
                    tmp_4++;
                    if (this->A[tmp_X][tmp_Y]._4>winLenghth-2) return 1;
                }
            }
        }
    }

    for (int i = 1; i<winLenghth; i++){
        if (i!=0){
            tmp_X = X-i;
            tmp_Y = Y+i;
            if (!(tmp_X<0 or tmp_X>=this->X or tmp_Y<0 or tmp_Y>=this->Y)){
                if (tmp_C==this->A[tmp_X][tmp_Y].skin){
                    this->A[tmp_X][tmp_Y]._7++;
                    tmp_7++;
                    if (this->A[tmp_X][tmp_Y]._7>winLenghth-2) return 1;
                }
            }
        }
    }

    this->A[X][Y]._8=tmp_8;
    this->A[X][Y]._9=tmp_9;
    this->A[X][Y]._6=tmp_6;
    this->A[X][Y]._3=tmp_3;
    this->A[X][Y]._2=tmp_2;
    this->A[X][Y]._1=tmp_1;
    this->A[X][Y]._4=tmp_4;
    this->A[X][Y]._7=tmp_7;

    if (A[X][Y]._8>winLenghth-2) return 1;
    if (A[X][Y]._9>winLenghth-2) return 1;
    if (A[X][Y]._6>winLenghth-2) return 1;
    if (A[X][Y]._3>winLenghth-2) return 1;
    if (A[X][Y]._2>winLenghth-2) return 1;
    if (A[X][Y]._1>winLenghth-2) return 1;
    if (A[X][Y]._4>winLenghth-2) return 1;
    if (A[X][Y]._7>winLenghth-2) return 1;

    return 0;
}

bool Field::End()
{
    bool tmp = 0;
    for(int i = 0; i < this->X; i++){
        for(int j = 0; j < this->Y; j++){
            tmp = tmp or this->A[i][j].skin=='_';
        }
    }
    return !tmp;
}

bool checkPlayers(Player B[], int count){
    int tmp = 0;
    for(int i = 0; i<count; i++){
        if (B[i].active==1) tmp++;
    }
    if (tmp<2) return 0;
    return 1;
}



int main()
{
    for (;1;)
    {
        int x=51, y=51, count=51, winLenghth=51, X=-1, Y=-1, winPos=0;
        char cX='_', cY='_';
        string next;
        bool gameRunning = 1;
        srand(time(0));

        while (x>50 or y>50) {
            system("cls");
            cout << "Enter X and Y of field (50-maximum)  >>>  ";
            cin >> x >> y;
        }
        Field A(x, y);

        while (count>y or count<2) {
            system("cls");
            cout << "Enter number of players (Y-maximum)  >>>  ";
            cin >> count;
        }
        Player B[count];
        for (int i = 0; i<count; i++) {
            char tmpSkin = '_';
            while (tmpSkin=='_'){
                system("cls");
                cout << "Enter skin of player " << i+1 << " >>>  ";
                cin >> tmpSkin;}
            B[i].skin = tmpSkin;
            B[i].active = 1;
            B[i].numerator = i;
        }

        while (winLenghth>x or winLenghth>y or winLenghth<2) {
            system("cls");
            cout << "Enter lenghth of line of figures to win (min(x,y) = maximum)  >>>  ";
            cin >> winLenghth;
        }

        system("cls");
        cout << "Generating move  s sequense";

        for (int i = 0; i<count; i++){
            int tmp = rand()%(count-i);
            int tmpNumerator;
            bool tmpActive;
            char tmpSkin;
            tmpSkin=B[count-tmp-1].skin;
            tmpActive=B[count-tmp-1].active;
            tmpNumerator=B[count-tmp-1].numerator;
            B[count-tmp-1].skin=B[i].skin;
            B[count-tmp-1].active=B[i].active;
            B[count-tmp-1].numerator=B[i].numerator;
            B[i].skin=tmpSkin;
            B[i].active=tmpActive;
            B[i].numerator=tmpNumerator;
        }

        for(int i = 0; gameRunning; ){
            while (X>x or Y>y or X<0 or Y<0 or A.A[X][Y].skin!='_') {
                A.Print(B, count, i);
                cout << "Enter your move(X, Y) >>> ";
                cin >> cX >> cY;
                if (cX<'a') {X=cX-65;} else {X=cX-71;}
                if (cY<'a') {Y=cY-65;} else {Y=cY-71;}
            }
            A.Move((X), (Y), B[i]);
            if(A.Check(X, Y, winLenghth)) {
                B[i].active=0;
                B[i].leaderboardPos=winPos;
                winPos++;
            }
            gameRunning=gameRunning*checkPlayers(B, count);
            if (A.End()) gameRunning = 0;
            if (i>=(count-1)) i=-1;
            X=-1;
            Y=-1;
            cX='_';
            cY='_';
            i++;
            while (!B[i].active){
                i++;
            }
        }

        system("cls");
        for (int i = 0; i<51; i++){
            for (int j = 0; j<count; j++){
                if (B[j].leaderboardPos==i) {
                    B[j].print();
                    cout << endl;
                }
            }
        }
        cout << "Next?(Enter something) >>> ";
        cin >> next;

        system("cls");
        cout << "Play again?(Enter something) >>> ";
        cin >> next;
    }

    return 0;
}
