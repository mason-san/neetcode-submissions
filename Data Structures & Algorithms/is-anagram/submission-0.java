class Solution {
    public boolean isAnagram(String s, String t) {
        //two hashmaps with their frequences (Character: Integer) for both the strings. 
        HashMap<Character, Integer> chars1 = new HashMap<>(); 
        HashMap<Character, Integer> chars2 = new HashMap<>(); 

        if (s.length() != t.length()){
            return false; 
        }

        for(int i = 0 ; i < s.length();i++){
            
            //Check if the key is already in the hashmap 
            chars1.put(s.charAt(i), chars1.getOrDefault(s.charAt(i), 0) + 1);

            //check for 2nd string 
            chars2.put(t.charAt(i), chars2.getOrDefault(t.charAt(i), 0) + 1); 
        }


        if (chars1.equals(chars2)){
            return true; 
        }
        
        return false; 
    }
}
