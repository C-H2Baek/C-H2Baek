import javax.swing.*;
import java.awt.*;
public class ContentPaneEx extends JFrame{
	public ContentPaneEx() {
		setTitle("ContentPane¿Í JFrame");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container contentPane = getContentPane();
		contentPane.setBackground(Color.ORANGE);
		contentPane.setLayout(new FlowLayout(FlowLayout.LEFT, 30, 40));
		contentPane.setLayout(new FlowLayout(FlowLayout.LEFT, 30, 40));
		contentPane.add(new JButton("OK"));
		contentPane.add(new JButton("Cancle"));
		contentPane.add(new JButton("Ignore"));
		contentPane.add(new JButton("OK"));
		contentPane.add(new JButton("Cancle"));
		contentPane.add(new JButton("Ignore"));
		contentPane.add(new JButton("OK"));
		contentPane.add(new JButton("Cancle"));
		contentPane.add(new JButton("Ignore"));
		contentPane.add(new JButton("OK"));
		contentPane.add(new JButton("Cancle"));
		contentPane.add(new JButton("Ignore"));
		
		setSize(300, 150);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new ContentPaneEx();
	}
}
