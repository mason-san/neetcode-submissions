class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] tmp = new int[2]; 
        HashMap<Integer, Integer> mapper = new HashMap<>(); 

        for(int i = 0 ; i < nums.length; i++){
            //I got the difference. 
            int diff = target - nums[i]; 
            
            //if difference is there in hashmap
            if (mapper.containsKey(diff)){
                //I have to get the value 
                tmp = new int[] {mapper.get(diff), i};
                break;
            } else {
                //else store the current element and its index and continue.
                mapper.put(nums[i], i); 
            }
        }

        return tmp; 
    }
}
