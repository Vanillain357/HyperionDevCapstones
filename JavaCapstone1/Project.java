public class Project {
	
	// Attributes
	String projectNumber;
	String projectName;
	String buildingType;
	String buildingAddress;
	String erfNumber;
	int totalFee;
	int paidFee;
	String dueDate;
	Person architect;
	Person contractor;
	Person customer;
	boolean finalized = false;
	String completionDate = "In Progress";
	
	// Constructor
	public Project(String projectNumber, String projectName, String buildingType, String buildingAddress, String erfNumber, 
			int totalFee, int paidFee, String dueDate, Person customer, Person architect, Person contractor) {
		this.projectNumber = projectNumber;
		this.projectName = projectName;
		this.buildingType = buildingType;
		this.buildingAddress = buildingAddress;
		this.erfNumber = erfNumber;
		this.totalFee = totalFee;
		this.paidFee = paidFee;
		this.dueDate = dueDate;
		this.customer = customer;
		this.architect = architect;
		this.contractor = contractor;
	}
	
	// Getters
	public int getTotalFee() {
		return totalFee;
	}
	
	public int getPaidFee() {
		return paidFee;
	}
	
	// Setters
	public void setDueDate(String newDueDate) {
		dueDate = newDueDate;
	}
	
	public void setFinalized(boolean completeness) {
		finalized = completeness;
	}
	
	public void setCompletionDate(String dateCompleted) {
		completionDate = dateCompleted;
	}
	
	// Methods
	public void paymentReceived(int amountPaid) {
		paidFee += amountPaid;
	}
	
	public String toString() {
		String objectString = "Project Number: " + projectNumber;
		objectString += "\nProject Name: " + projectName;
		objectString += "\n\nBuilding Type: " + buildingType;
		objectString += "\nPhysical Construction Address: " + buildingAddress;
		objectString += "\nERF Number: " + erfNumber;
		objectString += "\n\nTotal Project Fee: R" + totalFee;
		objectString += "\nFee Paid to Date: R" + paidFee;
		objectString += "\n\nDue Date: " + dueDate;
		objectString += "\nCompletion Date: " + completionDate;
		objectString += "\n\n\tCustomer's Details\n" + customer;
		objectString += "\n\n\tArchitect's Details\n" + architect;
		objectString += "\n\n\tContractor's Details\n " + contractor;
		
		return objectString;
	}
}