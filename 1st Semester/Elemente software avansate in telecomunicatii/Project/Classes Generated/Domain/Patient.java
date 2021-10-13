package Domain;

import java.util.*;

/**
 * 
 */
public class Patient extends User {

    /**
     * Default constructor
     */
    public Patient() {
    }

    /**
     * 
     */
    public Address hospitalAddress;

    /**
     * 
     */
    public Blood blood = null;

    /**
     * 
     */
    public Double requestedBloodQuantity;

    /**
     * 
     */
    public List<Donation> donations;

    /**
     * 
     */
    public Integer urgency;

}