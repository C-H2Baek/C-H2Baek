import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.util.HashMap;

public class OpenChallenge_13 extends JFrame{

	JLabel user = new JLabel("@");
	JLabel monster= new JLabel("M");
	JLabel hahaha = new JLabel("메롱");
	Point userPoint = new Point(500,350);
	Point monsterPoint = new Point(0,0);
	boolean gameStop = false;
	
	Container c = null;

	public OpenChallenge_13() {
		
		c = getContentPane();
		c.setLayout(null);
		c.setFocusable(true);
		c.requestFocus();
		c.addKeyListener(new UserT());

		Thread userT = new Thread(new UserT());
		Thread monsterT = new Thread(new MonsterT());
		
		userT.start();
		monsterT.start();
		
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(1920, 1080);
		setTitle("Run Away from Monster");
	}

	class UserT extends KeyAdapter implements Runnable{
		
		UserT(){
			user.setLocation(userPoint);
			user.setSize(20,20);
			c.add(user);
			c.add(hahaha);
			hahaha.setSize(30,30);
		}
		
		public void keyPressed(KeyEvent e) {
			int keyCode = e.getKeyCode();
			
			if(keyCode == KeyEvent.VK_RIGHT) {
				userPoint.x = userPoint.x += 10;
			}
			else if(keyCode == KeyEvent.VK_LEFT) {
				userPoint.x = userPoint.x -= 10;
			}
			else if(keyCode == KeyEvent.VK_UP) {
				userPoint.y = userPoint.y -= 10;
			}
			else if(keyCode == KeyEvent.VK_DOWN) {
				userPoint.y = userPoint.y += 10;
			}
			user.setLocation(userPoint);
			repaint();
		}
	
		// 그냥 넣은 기능
		public void run() {
			while(true) {
				try {
					if(gameStop == true)
						return;
					
					int x = userPoint.x - 5;
					int y = userPoint.y - 20;
					hahaha.setLocation(x, y);
					hahaha.setVisible(true);
					repaint();
					Thread.sleep(2000);
					hahaha.setVisible(false);
					Thread.sleep(5000);
				} catch (InterruptedException e) {
					return;
				}
			}
		}
	}
	
	class MonsterT implements Runnable{
		
		MonsterT(){
			monster.setLocation(monsterPoint);
			monster.setSize(20,20);
			monster.setForeground(Color.red);
			c.add(monster);
		}
		
		public void run() {
			while(true) {
				try {
					if(check()) {
						System.out.println("You've Catched!");
						gameStop = true;
						return;
					}
					
					if(userPoint.x > monsterPoint.x)
						monsterPoint.x = monsterPoint.x + 5;
					else if(userPoint.x < monsterPoint.x)
						monsterPoint.x = monsterPoint.x - 5;
				
					if(userPoint.y > monsterPoint.y)
						monsterPoint.y = monsterPoint.y + 5;
					else if(userPoint.y < monsterPoint.y)
						monsterPoint.y = monsterPoint.y - 5;
					Thread.sleep(50);
					
					monster.setLocation(monsterPoint);
					repaint();
				}catch(InterruptedException e) {
					return;
				}
			}
		}
	}
	
	synchronized public boolean check() {
		if(userPoint.equals(monsterPoint)) {
			return true;
		}
		return false;
	}
	public static void main(String[] args) {
		new OpenChallenge_13();
	}
}
	