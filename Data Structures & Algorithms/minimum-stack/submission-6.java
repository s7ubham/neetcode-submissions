class MinStack {

    List<Integer> testArray;
    List <Integer> minimumStack;
    int currentIndex;

    public MinStack() {
          testArray = new ArrayList<Integer>();
          minimumStack = new ArrayList<Integer>();
          currentIndex=-1;
          
        
    }
    
    public void push(int val) {
        testArray.add(val);
        currentIndex+=1;
        if (minimumStack .isEmpty() ||  minimumStack.get(minimumStack.size()-1)>=val){
            minimumStack.add(val);
            //System.out.println(minimumStack);


        }

    }
    
    public void pop() {
        
        if (minimumStack.get(minimumStack.size()-1).equals(testArray.get(currentIndex))){
            minimumStack.remove(minimumStack.size()-1);
        }

        testArray.remove(currentIndex);
        currentIndex-=1;

        // System.out.println(minimumStack);
    }
    
    public int top() {
        return  testArray.get(currentIndex).intValue();
        
    }
    
    public int getMin() {
        return minimumStack.get(minimumStack.size()-1);
        
    }
}
