package oopProjects;

public class SavingsAccount {
	 int accountNo;
	 float balance;
	 int pin;
	 
	 public void Deposit(int amount) {
		 if(amount > 0) {
			 balance = balance + amount;
		 }
		 else {
			 System.out.println("Invalid deposit amount");
		 }
	 }
	 
	 public void Withdraw(int withdrawAmount) {
		 if(withdrawAmount <= balance) {
			 balance = balance - withdrawAmount;
		 }
		 else {
			 System.out.println("Insufficient funds");
		 }
	 }
 


}
