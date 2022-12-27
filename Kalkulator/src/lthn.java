
import java.util.Scanner;


public class lthn {
    public static void main(String[] args) {
        String nama;
        int umur;
        
        Scanner input = new Scanner(System.in);
        System.out.println("Masukkan nama : ");
        nama = input.nextLine();
        
        System.out.println("Masukkan umur : ");
        umur = input.nextInt();
        
        System.out.println("Nama : " + nama);
        System.out.println("umur : " + umur);
    }
    
}

