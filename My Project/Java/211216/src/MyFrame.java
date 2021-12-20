import javax.swing.*;

public class MyFrame extends JFrame{
	public MyFrame() {
		setTitle("Title");
		setSize(300, 300);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		MyFrame frame = new MyFrame();
		MyFrame frame2 = new MyFrame();
	}
}
