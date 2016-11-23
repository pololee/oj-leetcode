package javasolutions.learn;

import java.util.Arrays;
import java.util.Comparator;

public class Employee implements Comparable<Employee> {
  private int id, age;
  private String name;
  private int salary;

  public int getId() {
    return id;
  }

  public int getAge() {
    return age;
  }

  public String getName() {
    return name;
  }

  public int getSalary() {
    return salary;
  }

  public Employee(int id, String name, int age, int salary) {
    this.id = id;
    this.age = age;
    this.name = name;
    this.salary = salary;
  }

  @Override
  public int compareTo(Employee other) {
    // return 
    // < 0  less than
    // = 0 equal
    // > 0 larger than
    return (this.id - other.id);
  }

  @Override
  public String toString(){
    String str = String.format("[id=%d, name=%s, age=%d, salary=%d]", this.id, this.name, this.age, this.salary);
    return str;
  }

  public static Comparator<Employee> SalaryComparator = new Comparator<Employee>() {
    @Override
    public int compare(Employee e1, Employee e2) {
      return (e1.getSalary() - e2.getSalary());
    }
  };

  public static Comparator<Employee> AgeComparator = new Comparator<Employee>() {
    @Override
    public int compare(Employee e1, Employee e2) {
      return e1.getAge() - e2.getAge();
    }
  };

  public static void main(String[] args) {
    Employee[] employees = new Employee[4];
    employees[0] = new Employee(10, "Mikey", 25, 10000);
    employees[1] = new Employee(20, "Arun", 29, 20000);
    employees[2] = new Employee(5, "Lisa", 35, 5000);
    employees[3] = new Employee(1, "Pankaj", 32, 50000);

    Arrays.sort(employees);
    System.out.println("Sort employees by ID");
    for(int i = 0; i < employees.length; i++) {
      System.out.println(employees[i].toString());
    }

    Arrays.sort(employees, Employee.SalaryComparator);
    System.out.println("Sort employees by Salary");
    for(int i = 0; i < employees.length; i++) {
      System.out.println(employees[i].toString());
    }
  }
}