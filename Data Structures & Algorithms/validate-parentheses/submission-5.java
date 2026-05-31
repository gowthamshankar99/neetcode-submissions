class Solution {
    public boolean isValid(String s) {

        if(s.length() == 1)
            return false;
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

        // push values to stack if its opening brasis 

        // if you find a closing brasis - pop from the stack and verify 

        // check if stack is empty
    }
}
