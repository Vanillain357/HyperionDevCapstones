import java.util.Scanner;

public class Program{
	
	static Scanner input = new Scanner(System.in);
	
	public static void main(String [] args) {
		
		System.out.println("\t\tPoised Project Management\n");
		
		// prompt the user to enter the details of the 3 required people and the project
		Person customer = addCustomer();
		Person architect = addArchitect();
		Person contractor = addContractor();
		Project firstProject = addProject(customer, architect, contractor);
		
		// keep presenting the main menu until the user finalizes the project
		do {
			switch (mainMenu()) {
				case 1:
					System.out.println("Sorry, in this update only one prject at a time is supported.");
					break;
					
				case 2:
					changeDueDate(firstProject);
					break;
					
				case 3:
					recordPayment(firstProject);
					break;
					
				case 4:
					updateContractorDetails(contractor);
					break;
					
				case 5:
					finalize(firstProject);
					break;
					
				default:
					System.out.println("Sorry, that is not a valid input.");
					break;
			}
		} while (true);
	}	
	
	public static int mainMenu() {		
		System.out.println("Welcome! Please select an option below:"
				+ "\n  1) Add a new project"
				+ "\n  2) Change the due date of the project"
				+ "\n  3) Record a payment towards the project"
				+ "\n  4) Update the contractor's contact details"
				+ "\n  5) Finalize the project");
		int mainMenuChoice = input.nextInt();
		
		return mainMenuChoice;
	}
	
	// declaring methods to add people to the project
	public static Person addCustomer() {
		System.out.println("Here at Poised we know that the most important part of a project is the people involved"
				+ "\nAnd none more so than the customer! Please start by entering the customer's details below"
				+ "\nWhat is the customer's name?");
		String customerName = input.nextLine();
		System.out.println("What is the customer's telephone number?");
		String customerNumber = input.nextLine();
		System.out.println("What is the customer's email address?");
		String customerEmail = input.nextLine();
		System.out.println("What is the customer's home address?");
		String customerAddress = input.nextLine();
		
		Person customer = new Person(customerName, customerNumber, customerEmail, customerAddress);
		return customer;
	}
	
	public static Person addArchitect() {
		System.out.println("And now on to the architect.\nWhat is the architect's name?");
		String architectName = input.nextLine();
		System.out.println("What is the architect's telephone number?");
		String architectNumber = input.nextLine();
		System.out.println("What is the architect's email address?");
		String architectEmail = input.nextLine();
		System.out.println("What is the architect's home address?");
		String architectAddress = input.nextLine();
		
		Person architect = new Person(architectName, architectNumber, architectEmail, architectAddress);
		return architect;
	}
	
	public static Person addContractor() {
		System.out.println("Last, but not least, the contractor.\nWhat is the contractor's name?");
		String contractorName = input.nextLine();
		System.out.println("What is the contractor's telephone number?");
		String contractorNumber = input.nextLine();
		System.out.println("What is the contractor's email address?");
		String contractorEmail = input.nextLine();
		System.out.println("What is the contractor's home address?");
		String contractorAddress = input.nextLine();
		
		Person contractor = new Person(contractorName, contractorNumber, contractorEmail, contractorAddress);
		return contractor;
	}
	
	// declaring a method to add a project
	public static Project addProject(Person customer, Person architect, Person contractor) {
		System.out.println("Now let's get some information on the project.\nWhat is the project number?");
		String projectNumber = input.nextLine();
		System.out.println("What is the project name?");
		String projectName = input.nextLine();
		System.out.println("What type of building will be constructed?");
		String projectType = input.nextLine();
		System.out.println("What will the physical address of the building be?");
		String projectAddress = input.nextLine();
		System.out.println("What is the ERF number?");
		String projectERF = input.nextLine();
		System.out.println("What is the total fee?");
		int projectFee = input.nextInt();
		System.out.println("How much has been paid so far?");
		int projectPaid = input.nextInt();
		input.nextLine();
		System.out.println("When is the deadline for the project?");
		String projectDue = input.nextLine();
		
		// if no project name is given, create one from the type and customer surname
		if (projectName.isBlank()) {
			String[] arrCustomerName =  customer.getName().split(" ");
			projectName = projectType + " " + arrCustomerName[arrCustomerName.length - 1];
		}
		
		
		Project firstProject = new Project(projectNumber, projectName, projectType, projectAddress, projectERF, 
				projectFee, projectPaid, projectDue, customer, architect, contractor);
		
		System.out.println("Project added.");
		return firstProject;
	}
	
	// declaring methods for each main menu option
	public static void changeDueDate(Project firstProject) {
		input.nextLine();
		System.out.println("What is the new due date for the project?");
		String newDueDate = input.nextLine();
		firstProject.setDueDate(newDueDate);
		System.out.println("Due date changed.");
	}
	
	// when a payment is received, add it to the "paidFee" attribute and print out the total paid to date
	public static void recordPayment(Project firstProject) {
		System.out.println("What was the amount of the payment received?");
		int amountPaid = input.nextInt();
		firstProject.paymentReceived(amountPaid);
		System.out.println("Payment received. The total of payments made to date is R" + firstProject.getPaidFee());
	}
	
	public static void updateContractorDetails(Person contractor) {
		input.nextLine();
		System.out.println("What is the contractor's new telephone number?");
		String newNumber = input.nextLine();
		System.out.println("What is the contractor's new email address?");
		String newEmailAddress = input.nextLine();
		contractor.setPhoneNumber(newNumber);
		contractor.setEmailAddress(newEmailAddress);
		System.out.println("Contact details updated.");
	}
	
	public static void finalize(Project firstProject) {
		// if the total fee has not been paid when the project is finalized, print an invoice
		if (firstProject.getTotalFee() > firstProject.getPaidFee()) {
			System.out.println("**INVOICE**"
					+ "\nPERSON RESPONSIBLE FOR PAYEMNT: " + firstProject.customer.getName()
					+ "\nTELEPHONE NUMBER: " + firstProject.customer.getPhoneNumber()
					+ "\nEMAIL ADDRESS: " + firstProject.customer.getEmailAddress()
					+ "\nHOME ADDRESS: " + firstProject.customer.getHomeAddress()
					+ "\n\nTOTAL FEE: R" + firstProject.getTotalFee()
					+ "\nPAID FEE: R" +firstProject.getPaidFee()
					+ "\nAMOUNT PAYABLE: R" + (firstProject.getTotalFee() - firstProject.getPaidFee())
					+ "\n");
		}
		
		// update the completion date to the current date and set the "finalized" attribute to true
		firstProject.setCompletionDate(java.time.LocalDate.now().toString());
		firstProject.setFinalized(true);
		
		// print out all of the details of the project and the people and end the program
		System.out.println(firstProject);
		System.exit(0);
	}
}