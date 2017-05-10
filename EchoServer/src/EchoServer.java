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
		
		// 데이터를 보내는 레퍼런스
		OutputStream out = null;
		DataOutputStream dos = null;
		
		// 데이터를 받을 레퍼런스
		InputStream in = null;
		DataInputStream din = null;
		
		Scanner scanner = new Scanner(System.in);
		try  
		{ 
			serversocket = new ServerSocket(80); 
			System.out.println("서버 준비 완료"); 
			 
			socket = serversocket.accept(); 
			System.out.println("클라이언트 연결완료");
			 
			// 데이터를 보낼 준비 
			out = socket.getOutputStream(); 
			dos = new DataOutputStream(out); 
			 
			// 데이터를 받을 준비 
			in = socket.getInputStream(); 
			din = new DataInputStream(in); 
			 
			while(true){ 
				String userMsg = din.readUTF(); 
				System.out.println("사용자 메시지:" + userMsg); 
				if(userMsg.equals("EXIT"))break; 
				 
				// 받을 메시지 다시 전송 
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
			// 읽는 스트림 종료 
			if( din != null ){  
				try{din.close();} 
				catch(Exception e){} 
			} 
			 
			if( in != null ){  
				try{in.close();} 
				catch(Exception e){} 
			} 
			 
			// 쓰는 스트림 종료 
			if( dos != null ){  
				try{din.close();} 
				catch(Exception e){} 
			} 
			 
			if( out != null ){  
				try{in.close();} 
				catch(Exception e){} 
			} 
			 
			// 네트워크 종료 
			if( socket != null ){  
				try{socket.close();} 
				catch(Exception e){} 
			} 
		}// end finally 
		
	}

}
