dd:second-child / dd:nth-of-type(2) 두번째 dd태그
p:not(.foo) class가 foo가 아닌 p태그
li:nth-of-type(2n+3) 2n+3번째 li태그
div > * div 이하 모든 요소
span[data-item] 어트리뷰트가 data-item인 span태그
p ~ span p와 동등한(형제인) span 태그
:enabled disabled가 아닌 태그
#one, #two, #five, #six, #nine id가 다음과 같은 태그
a + span a와 바로 옆에 붙은 span태그(인접형제 선택자)
div#foo > div.foo id가 foo인 div 태그 아래 class가 foo인 div 태그
div div span + code:not(.foo) div 태그 아래 div 태그 아래 span 태그와 형제 요소 중에 class가 foo가 아닌 태그

copy-copy selector 해주면 편한데 이게 안 되는 사이트도 있음.
상세한 방법은 css selector 공식 문서에서 확인 가능