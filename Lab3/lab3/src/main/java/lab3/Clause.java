package lab3;
import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;


/**
 * Clause Definition
 */

public class Clause {
  // Lists of strings
  public Set<String> p;
  public Set<String> n;

  public Clause(String s){
    Set<String> sentence = createSet(s);

    p = new HashSet<>();
    n = new HashSet<>();
    
    // Interpret negation
    sentence.forEach(str -> {
      if(str.charAt(0) == '-'){
        n.add(str.substring(1));
      }
      else{
        p.add(str);
      }
    });
  }
  
  public Clause(){
    
  }

  public static Set<String> intersection(Set<String> s1, Set<String> s2){
    Set<String> c = new HashSet<>(s1);
    c.retainAll(s2);

    return c;
  }

  public static Set<String> union(Set<String> s1, Set<String> s2){
    Set<String> c = new HashSet<>(s1);
    c.addAll(s2);

    return c;
  }

  public static Set<String> createSet(String string){
    return new HashSet<>(Arrays.asList(string.split(" ")));
  }

  void print(){
    System.out.println(" p = " + p.toString());
    System.out.println(" n = " + n.toString());
  }

  void print(String prefix){
    System.out.println(prefix + " = ");
    System.out.println(" p = " + p.toString());
    System.out.println(" n = " + n.toString());
  }
}
