package oopProjects;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//creating a object for SavingsAccount class
		SavingsAccount account = new SavingsAccount();
		
		account.accountNo = 12343;
		account.balance = 342;
		account.pin = 4321;
		System.out.println("Account number is:  " + account.accountNo);
		
		
		SavingsAccount a2 = new SavingsAccount();
		a2.accountNo = 34234;
		a2.balance = 453;
		a2.pin = 4522;
		
		System.out.println("Account number is:  " + a2.accountNo);
		
	}

}
