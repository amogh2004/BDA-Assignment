import java.util.Scanner;

class MethodOne {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    double f;
    double pi = 1;

    System.out.println("Enter the number of iterations: ");
    int n = sc.nextInt();

    for(int i = n; i > 1; i--) {
      f = 2;
      for(int j = 1; j < i; j++){
         f = 2 + Math.sqrt(f);
      }
      f = Math.sqrt(f);
      pi = pi * f / 2;
    }
    pi *= Math.sqrt(2) / 2;
    pi = 2 / pi;

    System.out.println("Aproximated value of PI= " +pi);
  }
}
