package Workshop2;

public class workshop2_3 {

public class BBSItem {
	int seqNo;  //일련번호 필드
	String winter;  //작성자 필드
	String writtenDate; //작성일자 필드
	String title; //제목필드
	String content; //내용필드
	BBSItem(int seqNo, String writer, String writtenDate,
			String title, String content){ //생성자
		this.seqNo=seqNo;
		this.writer=writer;
		this.writtenDate=writtenDate;
		this.title=title;
		this.content=content;
	}
	}
}
