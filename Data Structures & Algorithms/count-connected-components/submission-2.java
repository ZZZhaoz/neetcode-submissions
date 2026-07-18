class Solution {
    private List<Integer> par;
    private List<Integer> rank;
    public int countComponents(int n, int[][] edges) {
        par = new ArrayList<>();
        rank = new ArrayList<>();
        for (int i = 0; i < n; i ++){
            par.add(i);
            rank.add(1);
        }
        
        int res = n;
        for (int[] edge : edges) {
            res = res - union(edge[0], edge[1]);
        }
        return res;

    }

    private int find(int n1){
        int res = n1;
        while (res != par.get(res)) {
            par.set(res, par.get(par.get(res)));
            res = par.get(res);
        }
        return res;
    }

    private int union(int n1, int n2){
        int p1 = find(n1);
        int p2 = find(n2);

        if (p1 == p2){
            return 0;
        }

        if (rank.get(p1) > rank.get(p2)) {
            par.set(p2, p1);
            rank.set(p1, rank.get(p1) + rank.get(p2));
        } else {
            par.set(p1, p2);
            rank.set(p2, rank.get(p1) + rank.get(p2));
        }
        return 1;
    }
}
