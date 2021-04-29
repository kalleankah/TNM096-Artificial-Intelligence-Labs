package lab3;
import java.util.Set;
import org.apache.commons.lang3.builder.HashCodeBuilder;
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

  public Clause(Clause c){
    this.p = new HashSet<>(c.p);
    this.n = new HashSet<>(c.n);
  }

  void print(){
    for(String symbol : p){
      System.out.print(symbol + " ");
    }

    for(String symbol : n){
      System.out.print("-" + symbol + " ");
    }

    System.out.println("");
  }

  void print(String prefix){
    System.out.print(prefix);
    this.print();
  }

  // void print(){
  //   System.out.println(" p = " + p.toString());
  //   System.out.println(" n = " + n.toString());
  // }

  // void print(String prefix){
  //   System.out.println(prefix + " = ");
  //   System.out.println(" p = " + p.toString());
  //   System.out.println(" n = " + n.toString());
  // }

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

  public boolean isSubsetOrEqual(Clause a) {
    return a.p.containsAll(this.p) && a.n.containsAll(this.n);
  }

  public boolean isSubset(Clause a) {
    // return a.p.containsAll(this.p) && a.n.containsAll(this.n) && !(a.p.equals(this.p) && a.n.equals(this.n));
    return a.p.containsAll(this.p) && a.n.containsAll(this.n) && !a.equals(this);
  }

  @Override
  public boolean equals(Object obj){
    if (obj == null) {
      return false;
    }

    if (!Clause.class.isAssignableFrom(obj.getClass())) {
        return false;
    }

    Clause other = (Clause)obj;
    return other.p.equals(p) && other.n.equals(n);
  }

  @Override
  public int hashCode() {
    return new HashCodeBuilder(17, 37)
            .append(p)
            .append(n)
            .toHashCode();
  }
}