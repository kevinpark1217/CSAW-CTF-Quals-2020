import java.util.*;
import java.io.*;

public class Difib {

    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("ramblings"));

        while(in.hasNextLine()) {
            String ramble = in.nextLine();

            //Clean up rambles by removing symbols
            String[] stringArray = ramble.split("\\W+");
            String result = new String();
            for(int i = 0; i < stringArray.length; i++) result += stringArray[i];
            
            ramble = result.toLowerCase();
            if(ramble.length() <= 26) {
                //Remove j
                ramble = ramble.replace("j", "");
                System.out.println(ramble);
            }
        }

        in.close();
    }
}