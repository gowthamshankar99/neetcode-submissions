class MinStack {

    Stack<Integer> minStack;
    Stack<Integer> stack;

    public MinStack() {
        minStack = new Stack<>();
        stack = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);
        if(minStack.isEmpty() || val <= minStack.peek()) {
           minStack.push(val);
        }
    }
    
    public void pop() {
        if(stack.isEmpty()) return;
        int poppedValue = stack.pop();
        if(minStack.peek() == poppedValue) {
            minStack.pop();
        }
        //stack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
