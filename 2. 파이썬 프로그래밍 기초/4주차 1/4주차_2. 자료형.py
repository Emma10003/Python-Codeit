'''
변수의 자료형 (Variable Data Type) ---------------------------------------------------------------------

 > 변수
    python) name = "James"
    Java) Strin name = "James";
 
 > 함수
    python) def print_sum(a, b):
    Java) public void print_sum(int a, int b) { }

Why are they different?
: python은 간편함과 편리함을 추구 -> 프로그램 오류가 발생할 가능성이 높아짐.
: Java는 복잡하고 불편함 -> 대신 프로그램을 더 정밀하게 만들 수 있음. (정확한 위치에 부품이 들어가도록!)
    +) Java는 실행할 때 마다 전체 코드가 제대로 짜였는지를 확인함.
-------------------------------------------------------------------------------------------------------
 > Dynamic typing Language
    : 파이썬처럼 자료형을 미리 정해주지 않는 언어들. 자료형은 실행될 때 정해짐.
        -> 간결하고 편리함, 코드의 내용과 로직이 쉽게 이해됨.
        -> 작은 사이즈의 프로그램을 만들기 좋음.
        -> 컴퓨터적 구조가 생략되어 실행 속도는 느림 ~>> 실행속도에 민감하지 않으나 프로젝트에 사용!
    : 종류) 파이썬, 루비, 자바스크립트, php, 펄? 등
    >> 현재는 Dynamic typing 언어가 인기를 끌고 있다 (프로그래밍 언어 패러다임의 변화...)

 > Static typing Language
    : 코드 실행 전 자료형을 미리 정해줌.
        -> 명확하고 정교함, 컴퓨터적 구조가 한 눈에 들어옴.
        -> 제약, 규칙이 많음 ~>> 실수를 방지하고 체계적으로 설계 가능.
        -> 많은 사람이 협업하는, 규모가 크거나 복잡한 프로젝트에 적합한 언어.
        -> 컴퓨터적 구조를 적어주기 때문에 실행 속도 빠름
    : 종류) C, C++, Kotlin, Java 등
'''