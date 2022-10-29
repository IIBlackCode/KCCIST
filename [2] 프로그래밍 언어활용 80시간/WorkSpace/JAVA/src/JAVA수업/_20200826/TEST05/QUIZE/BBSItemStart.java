package JAVA수업._20200826.TEST05.QUIZE;
/*
 * 다음은 인터넷 게시판의 게시글을 표현하는 클래스이다. 
 */
public class BBSItemStart {
	public static void main(String[] args) {
		BBSItem b1 = new BBSItem("작성자 필드1","작성일자 필드","제목필드","내용필드");
		System.out.println(b1.toString());
		BBSItem b2 = new BBSItem("작성자 필드2","작성일자 필드","제목필드","내용필드");
		System.out.println(b2.toString());
		BBSItem b3 = new BBSItem("작성자 필드3","작성일자 필드","제목필드","내용필드");
		System.out.println(b3.toString());
		BBSItem b4 = new BBSItem("작성자 필드4","작성일자 필드","제목필드","내용필드");
		System.out.println(b4.toString());
	}
}
/*
일련번호에 해당하는 seqNo 필드의 값을 생성자 파라미터로 받는 것이 아니라, 
새로운 객체가 생성될 때마 다 자동으로 붙여지게 하려고 한다. 
처음으로 생성되는 BBSItem객체에는 1, 
두번째로 생성되는 BBSItem 객 체에는 2, 
이런 식으로 일련번호가 붙여지도록 이 클래스르 수정하여라.
*/
