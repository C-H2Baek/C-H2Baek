import javax.swing.*;
import java.awt.*;
public class BorderLayoutEx extends JFrame{
	public BorderLayoutEx() {
		setTitle("BorderLayout Simple");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container contentPane = getContentPane();
		contentPane.setLayout(new BorderLayout());
		
		contentPane.add(new JButton("Calculate"), BorderLayout.CENTER);
		contentPane.add(new JButton("Add"), BorderLayout.NORTH);
		contentPane.add(new JButton("Sub"), BorderLayout.SOUTH);
		contentPane.add(new JButton("Mul"), BorderLayout.EAST);
		contentPane.add(new JButton("Div"), BorderLayout.WEST);
		setSize(300, 200);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new BorderLayoutEx();
	}
}
