class Solution {
    public int findKthLargest(int[] nums, int k) {
        List<Integer> list = new ArrayList<>();
        for (int n:nums) {
            list.add(-n);
        }

        PriorityQueue<Integer> heap = new PriorityQueue<>(list);
        int ans = 0;
        int i = 0;
        while (i < k) {
            ans = heap.poll();
            i ++;
        }
        return -ans;
    }
}
