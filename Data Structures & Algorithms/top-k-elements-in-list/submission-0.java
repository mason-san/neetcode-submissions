class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        //resultant array 
        List<Integer> res = new ArrayList<>(); 
        //I need to create n buckets 
        HashMap<Integer, Integer> mapper = new HashMap<>(); 

        //now, this is the buckets
        List<List<Integer>> buckets = new ArrayList<>(nums.length);

        //loop to create the buckets 
        for(int i= 0 ; i < nums.length + 1; i++){
            buckets.add(new ArrayList<>()); 
        }

        //we have to loop through the array 
        for(int i = 0 ; i < nums.length; i++){

            //i need to make the hashmap like the integer must be 
            // the number 
            //and then its frequency 
            //put the number and if its a new number, put 0. otherwise put + 1. 
            mapper.put(nums[i], mapper.getOrDefault(nums[i], 0) + 1); 
           
        }

        //Now, I need to create the bucket 
        for(Map.Entry<Integer, Integer> entry: mapper.entrySet()) {
            //adding according to the bucket
            buckets.get(entry.getValue()).add(entry.getKey());
        }

        //Now let's traverse the buckets backwards 
        for(int i = nums.length; i > 0 && res.size() != k ; i--){
            //The inner loop of the elements in the bucket
            for(int j = 0; j < buckets.get(i).size(); j++){
                //add it to the resultant array. 
                //if the length of the resultant array is not equal to k 
                if (res.size() != k){
                    res.add(buckets.get(i).get(j)); 
                }
            }
        }


        //the final solution 
        int[] ans = new int[res.size()]; 

        for(int i = 0 ; i < res.size(); i++){
            ans[i] = res.get(i); 
        }

        return ans; 
    }
}
