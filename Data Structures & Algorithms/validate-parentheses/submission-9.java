class Solution {
    public boolean isValid(String s) {
        

        //Stack

        Stack<Character> stack = new Stack<Character>();
        char t = ' ';
        for(int i=0;i<s.length();i++) {
            if(s.charAt(i) == '}') {
                if(stack.isEmpty()) 
                    return false;
                t = stack.peek();
                if(t == '{') {
                    stack.pop();
                } else{
                    return false;
                }
            } else if(s.charAt(i) == ')') {
                if(stack.isEmpty()) 
                    return false;                
                t = stack.peek();
                if(t == '(') {
                    stack.pop();
                } else {
                    return false;
                }
            } else if(s.charAt(i) == ']') {
                if(stack.isEmpty()) 
                    return false;                
                t = stack.peek();
                if(t == '[') {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.add(s.charAt(i));
            } 
        }

        if(stack.isEmpty()) {
            return true;
        }

        return false;
         
    }
}