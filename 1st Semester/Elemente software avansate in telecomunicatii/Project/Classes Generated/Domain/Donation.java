package Domain;

import java.util.*;

/**
 * 
 */
public class Donation {

    /**
     * Default constructor
     */
    public Donation() {
    }

    /**
     * 
     */
    public Blood blood;

    /**
     * 
     */
    private Double bloodQuantity;

    /**
     * 
     */
    public Double plasmaQuantity = null;

    /**
     * 
     */
    public Double thrombocytesQuantity = null;

    /**
     * 
     */
    public Double redCellsQuantity = null;

    /**
     * 
     */
    private LocalDate donationDate;

    /**
     * 
     */
    public Map<String; Boolean> testResults = null;

    /**
     * 
     */
    private static void plasmaExp = 365;

    /**
     * 
     */
    private static void thrombocytesExp = 42;

    /**
     * 
     */
    private static void redCellsExp = 5;

    /**
     * 
     */
    public Long id;

    /**
     * 
     */
    private static Long idGen = 1;



    /**
     * @param donationDate 
     * @param bloodQuantity
     */
    public void Donation(LocalDate donationDate, Double bloodQuantity) {
        // TODO implement here
    }

    /**
     * @return
     */
    public Double getBloodQuantity() {
        // TODO implement here
        return null;
    }

    /**
     * @return
     */
    public LocalDate getDonationDate() {
        // TODO implement here
        return null;
    }

}