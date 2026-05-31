class Solution {
    public boolean isValid(String s) {
        // create a stack 
        Stack<Character> stack = new Stack<>();
        char popped = '.';

        for(int i=0;i<s.length();i++) {
            if(s.charAt(i) == '}') {
                if(!stack.isEmpty()) {
                    popped = stack.pop();
                    if(popped != '{')
                        return false;
                } else {
                    return false;
                }
            } else if(s.charAt(i) == ')') {
                if(!stack.isEmpty()) {
                    popped = stack.pop();
                    if(popped != '(')
                        return false;
                } else {
                    return false;
                }
            } else if(s.charAt(i) == ']') {
                if(!stack.isEmpty()) {
                    popped = stack.pop();                
                    if(popped != '[')
                        return false;
                } else 
                    return false;

            }
            else {
                stack.add(s.charAt(i));
            }
        }
        if(stack.isEmpty())
            return true;
        else 
            return false;
    }
}
