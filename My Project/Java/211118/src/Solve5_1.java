class TV {
	private int size;
	public TV(int size) {this.size = size;}
	protected int getSize() { return size; }
}

class ColorTV extends TV {
	private int color;
	public ColorTV(int size, int color) {
		super(size);
		this.color = color ;
	}
	protected int getColor() { return color; }
	public void printProperty() {
		System.out.println(getSize()+"��ġ" + color + "�÷�");
	}
}

class IPTV extends ColorTV{
	String ipAddress;
	public IPTV(String ip, int size, int colorSize) {
		super(size, colorSize);
		ipAddress=ip;
	}
	@Override
	public void printProperty() {
		System.out.print("���� IPTV�� " + ipAddress + "�ּ���");
		super.printProperty();
	}
}
public class Solve5_1{

	public static void main(String [] args) {
		IPTV iptv = new IPTV("192.1.1.2",32, 1024);
		iptv.printProperty();
	}
}