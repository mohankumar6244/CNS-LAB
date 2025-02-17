import java.util.Scanner;

public class CaesarCipherAfterA {

    public static String encrypt(String text, int s) {
        String result = "";
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    c = (char) (((c - 'A' + s) % 26) + 'A'); 
                } else {
                    c = (char) (((c - 'a' + s) % 26) + 'a');
                }
                if (c < 'a' || (Character.isUpperCase(c) && c < 'A')) {
                    c += 26; // Shift back if the letter wrapped around
                }
            }
            result += c;
        }
        return result;
    }

    public static String decrypt(String text, int s) {
        s = 26 - s; // Calculate the inverse shift
        return encrypt(text, s); 
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter plain text: ");
        String plainText = scanner.nextLine();
        System.out.print("Enter shift value: ");
        int shift = scanner.nextInt();

        String cipherText = encrypt(plainText, shift);
        System.out.println("Cipher text: " + cipherText);

        String decryptedText = decrypt(cipherText, shift);
        System.out.println("Decrypted text: " + decryptedText);

        scanner.close();
    }
}