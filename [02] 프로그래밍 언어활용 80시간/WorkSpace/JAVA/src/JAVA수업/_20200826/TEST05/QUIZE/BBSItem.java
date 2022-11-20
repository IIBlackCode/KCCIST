package JAVA수업._20200826.TEST05.QUIZE;
/*
 * 다음은 인터넷 게시판의 게시글을 표현하는 클래스이다. 
 */
public class BBSItem {
	static int seqNo; // 일련번호 필드
	String writer; // 작성자 필드
	String writtenDate; // 작성일자 필드
	String title; // 제목필드
	String content; // 내용필드

	public BBSItem(String writer, String writtenDate, String title, String content) {
		// TODO Auto-generated constructor stub
		seqNo++;
		this.writer = writer;
		this.writtenDate = writtenDate;
		this.title = title;
		this.content = content;
		System.out.println(seqNo);
		
	}

	@Override
	public String toString() {
		return "BBSItem [seqNo=" + seqNo + ", writer=" + writer + ", writtenDate=" + writtenDate + ", title=" + title
				+ ", content=" + content + "]";
	}

}

class SeqNo{
	int num;
	
	public void num() {
		num++;
	}
}
/*
일련번호에 해당하는 seqNo 필드의 값을 생성자 파라미터로 받는 것이 아니라, 
새로운 객체가 생성될 때마 다 자동으로 붙여지게 하려고 한다. 
처음으로 생성되는 BBSItem객체에는 1, 
두번째로 생성되는 BBSItem 객 체에는 2, 
이런 식으로 일련번호가 붙여지도록 이 클래스르 수정하여라.
*/
