package lab3;
import java.util.Set;
import java.util.Random;

/**
 * Lab3
 */

public final class Lab3{

  public static Clause resolution(Clause c1 ,Clause c2){
    Set<String> i1 = Clause.intersection(c1.p,c2.n);
    Set<String> i2 = Clause.intersection(c1.n,c2.p);

    if(i1.isEmpty() && i2.isEmpty()){
      return null;
    }
    
    if(!i1.isEmpty()){
      String[] arr = i1.toArray(new String[i1.size()]);
      int rand = new Random().nextInt(i1.size());
      String element = arr[rand];
      c1.p.remove(element);
      c2.n.remove(element);
    }
    else{
      String[] arr = i2.toArray(new String[i2.size()]);
      int rand = new Random().nextInt(i2.size());
      String element = arr[rand];
      c1.n.remove(element);
      c2.p.remove(element);
    }
    
    Clause u = new Clause();
    u.p = Clause.union(c1.p, c2.p);
    u.n = Clause.union(c1.n, c2.n);

    if(!Clause.intersection(u.p, u.n).isEmpty()){
      return null;
    }
    // According to lab instructions we should remove duplicates from U here
    // however U should not contain duplicates 
    return u;
  }

  //Default launch
  public static void main(String[] args){
    // __________________TASK A.1____________

    // String Test1A = "a b -c";
    // String Test1B = "c b";
    // String Test2A = "a b -c";
    // String Test2B = "d b -g";
    // String Test3A = "-b c t";
    // String Test3B = "-c z b";

    // Clause c1 = new Clause(Test1A);
    // Clause c2 = new Clause(Test1B);
    // Clause c3 = resolution(c1,c2);
    
    // c1.print("C1");
    // c2.print("C2");

    // if (c3 != null){
    //   c3.print("C3");
    // }
    // else{
    //   System.out.println("false");
    // }

    //____________________TASK A.2__________________
    
    
  } // Main

} // Lab3 Class
