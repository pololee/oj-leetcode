import java.util.*;
import java.io.*;
import java.math.*;
import java.text.*;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution szy = new Solution();
        String a = "I am using Hackerrank to improve programming";
        String b = "am Hackerrank to improve";
        System.out.print(Arrays.toString(szy.MissingWord(a, b)));
        
	}
 
}

class Solution{
    public String[] MissingWord(String a, String b) {
    	if (a == null || a.length() == 0) {
    		return new String[0];
    	}
    	
    	String[] atmp = a.split(" ");
    	boolean[] exist = new boolean[atmp.length];
    	int count = atmp.length;
    	
    	for (int i = 0; i < atmp.length; i++) {
    		if (b.indexOf(atmp[i]) != -1) {
    			exist[i] = true;
    			count --;
    		}
    	}
    	
    	String[] res = new String[count];
    	int index = 0;
    	for (int i = 0; i < atmp.length; i++) {
    		if (!exist[i]) {
    			res[index] = atmp[i];
    			index ++;
    		}
       	}
    	
    	return res;
    	
    }
    
}
