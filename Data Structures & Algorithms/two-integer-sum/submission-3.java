class Solution {
    public int[] twoSum(int[] nums, int target) {
    HashMap<Integer, Integer> numMap = new HashMap<>();
    Arrays.sort(nums);
    for (int i = 0; i < nums.length; i++) {
      int diff = target - nums[i];
      System.out.println(diff + " " + nums[i]);
      if (numMap.containsKey(diff)) {
        return (new int[]{numMap.get(diff), i});
      }
      numMap.put(nums[i], i);
    }
    throw new IllegalArgumentException("no solution exists");
  }
}
