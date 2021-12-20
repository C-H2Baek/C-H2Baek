import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class KeyListenerEx extends JFrame {
	private JLabel [] keyMessage;
	
	public KeyListenerEx() {
		setTitle("KeyListener 예제");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container c = getContentPane();
		c.setLayout(new FlowLayout());
		c.addKeyListener(new MyKeyListener());
				
		keyMessage = new JLabel [3];
		keyMessage[0] = new JLabel(" getKeyCode()   ");
		keyMessage[1] = new JLabel(" getKeyChar()   ");
		keyMessage[2] = new JLabel(" getKeyText()   ");
		
		for(int i=0; i<keyMessage.length; i++) {
			c.add(keyMessage[i]);
			keyMessage[i].setOpaque(true);
			keyMessage[i].setBackground(Color.YELLOW);
		}
		
		setSize(300,150);
		setVisible(true);
		
		// 컨텐트펜이 키 입력을 받을 수 있도록 포커스 강제 지정
		c.setFocusable(true);
		c.requestFocus();
	}
	
	// Key 리스너 구현

	class MyKeyListener extends KeyAdapter {
		public void keyPressed(KeyEvent e) {
			int keyCode = e.getKeyCode(); // 키 코드 알아내기
			char keyChar = e.getKeyChar(); // 키 문자 값 알아내기
			keyMessage[0].setText(Integer.toString(keyCode)); // 키 코드 출력
			keyMessage[1].setText(Character.toString(keyChar)); // 키 문자 출력 
			keyMessage[2].setText(KeyEvent.getKeyText(keyCode)); // 키 이름 문자 열 출력
			
			Container contentPane = (Container)e.getSource();
			if(e.getKeyChar() == '%')
				contentPane.setBackground(Color.YELLOW);
			else if(e.getKeyCode() == KeyEvent.VK_F1)
				contentPane.setBackground(Color.GREEN);
			
			System.out.println("KeyPressed"); // 콘솔창에 메소드 이름 출력
		}
		public void keyReleased(KeyEvent e) {
			System.out.println("KeyReleased"); // 콘솔창에 메소드 이름 출력
		}
		public void keyTyped(KeyEvent e) {
			System.out.println("KeyTyped"); // 콘솔창에 메소드 이름 출력
		}
	}
	
	public static void main(String [] args) {
		new KeyListenerEx();
	}
}
