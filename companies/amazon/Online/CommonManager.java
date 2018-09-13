import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;
import java.util.Stack;
class Employee {
    	int id;
    	List<Employee> reports = new ArrayList<Employee>();
    	public void setId(int val){
    		id = val;
    	}
    	public int getId(){
    		return id;
    	}
    	public void addReport(Employee emp){
    		reports.add(emp);
    	}
    	public List<Employee> getReports(){
    		return reports;
    	}
    
	


public class CommonManager {
	
	public  Employee comManager (Employee ceo,Employee emp1,Employee emp2){
		if(ceo==null || emp1==ceo || emp2 ==ceo) return null;
		
		Deque <Employee> e1 = new LinkedList<Employee>();
		Deque <Employee> e2 = new LinkedList<Employee>();
		Employee root = ceo;
		boolean hasEmp1 = dfs(root,emp1,e1);
		boolean hasEmp2 = dfs(root,emp2,e2);
		
		if (hasEmp1 && hasEmp2){
			int len1 = e1.size();
			int len2 = e2.size();
			if (len1 > len2){
				moveUp(e1,len1-len2);
			}else {
				moveUp(e2,len2-len1);
			}
			
			//e1 and e2 are in the same size now
			while (e1.size()>0 && e1.peek().getId() != e2.peek().getId()){
				e1.pop();
				e2.pop();
			}
			if (e1.size() > 0){
				return e1.peek();
			}
			
		}
		return null;

	}
	
	public  void moveUp(Deque<Employee> stack,int steps){
		while(steps > 0 && !stack.isEmpty()){
			stack.pop();
			steps--;
		}
	}
	public  boolean dfs(Employee root,Employee emp, Deque<Employee> stack){
		stack.offerFirst(root);
		if (root.getId() == emp.getId()){
			return true;
		}
		for (Employee em :root.getReports()){
			boolean result = dfs(em,emp,stack);
			if (result == true){
				return true;
			}
			
		}
		stack.pollFirst();
		return false;
	}
	
//will give wrong result for e1 or e2 not exit	
//	public Employee commonManager(Employee ceo, Employee e1, Employee e2){
//		Employee common = search(ceo, e1, e2);
//		if(common.getId() == ceo.getId()){
//			return null;
//		}
//		return common;
//	}
	//assume e1 e2 in the graph
//	public Employee search(Employee manager, Employee e1, Employee e2){
//		if(manager.getId() == e1.getId() || manager.getId() == e2.getId()){
//			return manager;
//		}
//		Employee m1 = null;
//		Employee m2 = null;
//
//		for(Employee em: manager.getReports()){
//			Employee result = search(em, e1, e2);
//			if(result != null){
//				if(m1 == null){
//					m1 = result;
//				} else {
//					m2 = result;
//					break;
//				}
//			}
//		}
//		if(m1 != null && m2 != null) return manager;
//		if(m1 == null && m2 == null) return null;
//		if(m1 == null) return m2;
//		if(m2 == null) return m1;
//		
//		return null;
//	}
  }
}
