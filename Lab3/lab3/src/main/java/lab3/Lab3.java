package lab3;
import java.util.Set;
import java.util.*;
import java.util.HashSet;
import java.util.Random;

/**
 * Lab3
 */

public final class Lab3{

  public static Clause resolution(Clause inC1 ,Clause inC2){
    Clause c1 = new Clause(inC1);
    Clause c2 = new Clause(inC2);
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

  public static void solver(Set<Clause> kb){
    Set<Clause> s;
    Set<Clause> kbCopy  = new HashSet<>();
    
    while(!kb.equals(kbCopy)){
      s = new HashSet<>();
      kbCopy = new HashSet<>(kb);


      for(Clause c1 : kb){
        for(Clause c2 : kb){
          if(!c1.equals(c2)){
            Clause c3 = resolution(c1,c2);
            if(c3 != null){
              // System.out.print("Resolvent found: ");
              // c3.print();
              s.add(c3);
            }
          }
        }
      }

    if(s.isEmpty()){
        // No resolution step was performed
        System.out.println("S is empty");
        return;
      }
      
      // System.out.println("S:");
      // printSet(kb);
      //Incorporate S into KB
      incorporate(s, kb);
      // System.out.println("KB:");
      // printSet(kb);
    }
  }

  public static void printSet(Set<Clause> s){
    for(Clause c : s){
      c.print();
    }
  }

  public static void incorporate(Set<Clause> s, Set<Clause> kb){
    for(Clause c : s){
      incorporateClause(c, kb);
    }
  }
  
  public static void incorporateClause(Clause a, Set<Clause> kb){
        // for(Clause b : kb){
    //   //b = movie ice -money
    //   //a = movie
    //   if(b.isSubsetOrEqual(a)){
    //     // Don't incorporate a into KB if there is already
    //     // a clause b which is a subset of a.
    //     return;
    //   }
    // }
    
    boolean willAddA = true;
    boolean hasToAddA = false;
    Iterator<Clause> iter = kb.iterator();
    while(iter.hasNext()){
      Clause b = iter.next();
      if(b.isSubsetOrEqual(a)){
        willAddA = false;
      }

      if(a.isSubset(b)){
        iter.remove();
        hasToAddA = true;
      }
    }
    
    // We need to add a if we have removed something from kb
    // because a was a subset of another clause in kb 
    if(willAddA || hasToAddA){
      kb.add(a);
    }
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
    // String TestSolveA = "-movie money";
    // String TestSolveB = "-movie -ice";

    // Clause c1 = new Clause(TestSolveA);
    // Clause c2 = new Clause(TestSolveB);
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

    // String A = "-sun -money ice";
    // String B = "-money ice movie";
    // String C = "-movie money";
    // String D = "-movie -ice";
    // String E = "movie";
    
    // Set<Clause> KB = new HashSet<>();
    // KB.add(new Clause(A));
    // KB.add(new Clause(E));
    // KB.add(new Clause(C));
    // KB.add(new Clause(D));
    // KB.add(new Clause(B));   
    
    // // System.out.println("Initial KB:");
    // // printSet(KB)

    // solver(KB);

    // System.out.println("Solved KB:");
    // printSet(KB);

    //____________________TASK B__________________

    Set<Clause> KB = new HashSet<>();
    // Nobody else could have been involved other than A, B and C
    KB.add(new Clause("A B C"));
    // C never commits a crime without A’s participation.
    KB.add(new Clause("C -C"));
    KB.add(new Clause("-C A"));
    //B does not know how to drive
    KB.add(new Clause("-B B"));
    KB.add(new Clause("-B A C"));

    solver(KB);

    printSet(KB);
       
  } // Main

} // Lab3 Class