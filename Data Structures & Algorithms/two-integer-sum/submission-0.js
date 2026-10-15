class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        
        const hashmap = new Map();

        for(var i=0 ; i<nums.length; i++){
            const middleNumber = target - nums[i]

            if(hashmap.has(middleNumber)){
                return[hashmap.get(middleNumber),i]
            }

            hashmap.set(nums[i], i)
        }
        
    }
}
