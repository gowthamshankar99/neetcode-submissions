class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();

        for(String token : tokens) {
            if(token.equals("+") || token.equals("*")|| token.equals("-") || token.equals("/")) {
                // get 2 values from stack 
                Integer value1 = stack.pop();
                Integer value2 = stack.pop();
                Integer newvalue = 0;
                
                if (token.equals("+"))
                    newvalue = value1+value2;
                else if (token.equals("-"))
                    newvalue = value2-value1;
                else if (token.equals("*"))
                    newvalue = value1*value2;
                else {
                    newvalue = value2/value1;
                }

                stack.push(newvalue);
            } else {
                stack.push(Integer.parseInt(token));
            }
        }

        return stack.peek();
    }
}
