public class Person {
	
	// Attributes
	String name;
	String phoneNumber;
	String emailAddress;
	String homeAddress;
	
	// Constructor
	public Person(String name, String phoneNumber, String emailAddress, String homeAddress) {
		this.name = name;
		this.phoneNumber = phoneNumber;
		this.emailAddress = emailAddress;
		this.homeAddress = homeAddress;
	}
	
	// Getters
	public String getName() {
		return name;
	}
	
	public String getPhoneNumber() {
		return phoneNumber;
	}
	
	public String getEmailAddress() {
		return emailAddress;
	}
	
	public String getHomeAddress() {
		return homeAddress;
	}
	
	// Setters
	public void setPhoneNumber(String newPhoneNumber) {
		phoneNumber = newPhoneNumber;
	}
	
	public void setEmailAddress(String newEmailAddress) {
		emailAddress = newEmailAddress;
	}
	
	// Methods
	public String toString() {
		String objectString = "Name: " + name;
		objectString += "\nTellephone Number: " + phoneNumber;
		objectString += "\nEmail Address: " + emailAddress;
		objectString += "\nPhysical Address: " + homeAddress;
		
		return objectString;
	}
}