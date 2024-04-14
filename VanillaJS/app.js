console.log("Hello, World!");
/**변수만들때 let, const, var차이
let 재선언 금지, 재할당 가능
const 재선언 금지, 재할당 금지
var 재선언 가능, 재할당 가능**/

//undefined=값이 정의되지 않음
//null=값이 없음
const amIFat = null;
const something = undefined;

//array ? list같은거
/**데이터를 나열하기 위한 방법 중 하나.
항상 [ ] 안에 콤마(,)로 데이터들을 나열한다. 변수도 쓰일 수 있고, boolean, text, 숫자 등 데이터 정렬이 가능하다.
ex) const daysOfWeek = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];

만약, 위의 변수에서 5번째 element 값을 알려주세요. 라고 한다면 어떻게 출력해야 할까?
ex) console.log(daysOfWeek[4]) 라고 해야 5번째 값을 출력할 수 있다.

왜?? 컴퓨터는 숫자를 0부터 세기 때문에, “mon”은 0번째라고 생각하면 된다.
JS의 주석처리는 //

위의 상태에서 daysOfWeek이란 변수에 하나의 값을 더 넣고 싶다면 다음과 같이한다.
ex) daysOfWeek.push(“holiday”) .push는 추가하는 기능.*/
