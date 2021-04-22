import java.util.Vector;

public class Lab3 {
  public class Literals{
      private char a;
      private char b;

      Literals(char a){
          this.a = a;
          this.b = !a;
      }

      public a(){
        return a;
      }
      public b(){
        return ()
      }
  }
  public class Clause{
    Literals n;
    Literals p;
    
    Clause(Boolean n, Boolean p){
      this.n = new Literals(n, !n);
      this.p = new Literals(false, false);
    }
    
  }
  //konstruktor som med lista av clauses?
  public Lab3(){
    System.out.println("No constructor implemented");
  }

  //funktion som löser resolvents, dvs tar två clauses och kalkylerar resolvent
  // public Clause Resolution(Clause firstClaus, Clause secondClause){
    
  }
  //fuktion som löser 

  //Default launch
  public static void main(String[] args){
    System.out.println("Hello World");
    Lab3 labber = new Lab3();
  }
}

