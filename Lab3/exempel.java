//Lab 2: RSA Cryptology
//Labborants: Oskar Johannesson
//            oskjo806
//            Isac Rydén
//            isary742

import java.math.BigInteger;
import java.util.Random;
import java.io.IOException;
import java.util.Scanner;

public class RSA{
    private  BigInteger n,e;     //variables bob sends to alice
    private  BigInteger p,q,d;   //variables bob keeps private
    private  Random r;
    private  BigInteger phi;
    private  BigInteger mess;
    private  BigInteger encMess;
    private  BigInteger decMess;
    private  int bitLength = 32;
    public  BigInteger temp1;

    public static void main(String[] args)throws IOException{
        RSA rsa = new RSA();

        rsa.CreateKey(rsa.p,rsa.q);
        rsa.EncryptMessage();
        rsa.DecryptMessage();
        
    }

    // functions to create keys
    public  void CreateKey(BigInteger chosenp, BigInteger chosenq) {
        n = chosenp.multiply(chosenq); // calculate n
        phi = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE));
        e = BigInteger.probablePrime(bitLength / 2, r);

        while (e.gcd(phi).compareTo(BigInteger.ONE) != 0) {
            e.add(BigInteger.ONE); // make sure gcd of e and phi are 1
        }

        d = e.modInverse(phi);     //calculate d
    }

    // function to encrypt
    public void EncryptMessage() {
        Scanner in = new Scanner(System.in);  
        System.out.print("Enter your message: ");  
        String message = in.nextLine();         // type message to encrypt  
        in.close();          
        
        mess = new BigInteger(message.getBytes());    // encryption algorithm
        
        //mess has to be smaller than n, if not mess is divided up into peices that are smaller than n

        encMess = mess.modPow(e,n); 
        //System.out.print("encrypted message is: " + encMess.toByteArray());  
    }

    // function to decrypt
    public void DecryptMessage() {
            decMess = encMess.modPow(d, n);     // Decrypt message
            String decMessage = new String(decMess.toByteArray());
            System.out.print("decrypted message is: " + decMessage);  

    }

    public RSA(){
        r = new Random();
        p = BigInteger.probablePrime(bitLength , r);
        q = BigInteger.probablePrime(bitLength , r);
    }

}