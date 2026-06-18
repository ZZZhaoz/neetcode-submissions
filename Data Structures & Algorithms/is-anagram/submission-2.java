class Solution {
    public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) {
            return false;
        }

        // Create frequency maps for both strings
        Map<Character, Integer> frequencyS = new HashMap<>();
        Map<Character, Integer> frequencyT = new HashMap<>();

        // Fill the frequency map for the first string
        for (char c : s.toCharArray()) {
            frequencyS.put(c, frequencyS.getOrDefault(c, 0) + 1);
        }

        // Fill the frequency map for the second string
        for (char c : t.toCharArray()) {
            frequencyT.put(c, frequencyT.getOrDefault(c, 0) + 1);
        }

        // Check if both maps are equal
        return frequencyS.equals(frequencyT);
    }
}
