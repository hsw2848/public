import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class EchoServer {
	
	public static void main(String[] arg) throws Exception{
		
		List<Socket> socketList = new ArrayList<Socket>();
		
		ServerSocket serversocket = null;
		Socket socket = null;
		
		// �����͸� ������ ���۷���
		OutputStream out = null;
		DataOutputStream dos = null;
		
		// �����͸� ���� ���۷���
		InputStream in = null;
		DataInputStream din = null;
		
		Scanner scanner = new Scanner(System.in);
		try  
		{ 
			serversocket = new ServerSocket(80); 
			System.out.println("���� �غ� �Ϸ�"); 
			 
			socket = serversocket.accept(); 
			System.out.println("Ŭ���̾�Ʈ ����Ϸ�");
			 
			// �����͸� ���� �غ� 
			out = socket.getOutputStream(); 
			dos = new DataOutputStream(out); 
			 
			// �����͸� ���� �غ� 
			in = socket.getInputStream(); 
			din = new DataInputStream(in); 
			 
			while(true){ 
				String userMsg = din.readUTF(); 
				System.out.println("����� �޽���:" + userMsg); 
				if(userMsg.equals("EXIT"))break; 
				 
				// ���� �޽��� �ٽ� ���� 
				dos.writeUTF(userMsg); 
				dos.flush();				 
			}// end while 
		}// end try 
		catch (Exception e) { 
			// TODO: handle exception 
			e.printStackTrace(); 
		}// end catch  
		finally 
		{ 
			// �д� ��Ʈ�� ���� 
			if( din != null ){  
				try{din.close();} 
				catch(Exception e){} 
			} 
			 
			if( in != null ){  
				try{in.close();} 
				catch(Exception e){} 
			} 
			 
			// ���� ��Ʈ�� ���� 
			if( dos != null ){  
				try{din.close();} 
				catch(Exception e){} 
			} 
			 
			if( out != null ){  
				try{in.close();} 
				catch(Exception e){} 
			} 
			 
			// ��Ʈ��ũ ���� 
			if( socket != null ){  
				try{socket.close();} 
				catch(Exception e){} 
			} 
		}// end finally 
		
	}

}
