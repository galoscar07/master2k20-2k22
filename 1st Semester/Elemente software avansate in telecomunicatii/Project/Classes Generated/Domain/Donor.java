package Domain;

import java.util.*;

/**
 * 
 */
public class Donor extends User {

    /**
     * Default constructor
     */
    public Donor() {
    }

    /**
     * 
     */
    public Donation currDonation;

    /**
     * 
     */
    public LocalDate currApointment = null;

    /**
     * 
     */
    public LocalDate lastDonationDate = null;

    /**
     * 
     */
    private List<Donation> donationHistory;


    /**
     * @param firstName 
     * @param lastName 
     * @param bDay 
     * @param address 
     * @param residence 
     * @param CNP 
     * @param username 
     * @param password
     */
    public void Donor(String firstName, String lastName, LocalDate bDay, Address address, Address residence, Long CNP, String username, String password) {
        // TODO implement here
    }

    /**
     * @param patient 
     * @return
     */
    public Donation donate(Optional<Patient> patient) {
        // TODO implement here
        return null;
    }

    /**
     * @return
     */
    public List<Donation> getDonationHistory() {
        // TODO implement here
        return null;
    }

    /**
     * @param donation
     */
    private void updateDonationHistory(Donation donation) {
        // TODO implement here
    }

}