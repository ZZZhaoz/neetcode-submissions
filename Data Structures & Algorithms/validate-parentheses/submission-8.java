class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        if (s.isEmpty()) {
            return true;
        }

        for (int i = 0; i < s.length(); i++) {
            char c  = s.charAt(i);
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            }

            if  (c == ')' || c == ']' || c == '}') {
                if (stack.isEmpty()) {
                    return false;
                }
                char d = stack.poll();
                if ((c == ')' && d != '(') ||
                        (c == ']' && d != '[') ||
                        (c == '}' && d != '{')) {
                    return false;
                }
            }
        }
        
        return stack.isEmpty();
    }   
}
