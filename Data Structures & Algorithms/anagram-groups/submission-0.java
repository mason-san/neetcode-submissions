class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>(); 
        //using hashmap to find anagrams of strings
        HashMap<String, List<String>> map = new HashMap<>(); 
        

        //looping through each string 
        for(int i = 0 ; i < strs.length; i++){
            //an integer array of size 26 
            int[] chars = new int[26]; 

            //now i'm pointing to one of the strings 
            //i need to get the character of every string. 
            for(int j = 0 ; j < strs[i].length(); j++){
                //character of the string
                char c = strs[i].charAt(j);

                //convert to number 
                int cNo = c - 'a'; 

                //update the array of 26 size
                chars[cNo] += 1; 
            }

            //now that i have the updated array with frequency of each of the character in the string 
            //add it to the hashmap
            //the key would be the string, and the value would be the list of strings. 
            // map.put(Arrays.toString(chars), strs[i])

            //use the hashmap as a way to group all the strings with the same number of characters 
            //if the key already exists in the hashmap 
           

           map.computeIfAbsent(Arrays.toString(chars), k -> new ArrayList<>()).add(strs[i]);
        }

        return new ArrayList<>(map.values()); 
    }
}
